import socket
import json
from question import question
# configuração do servidor
localIP = "127.0.0.1"
localPort = 20003
bufferSize = 1024

# array com jogadores
jogadores = []
# Perguntas
pergunta  = question('Sei lá qualquer coisa?',[('a',"sei la"), ('b',"talvez seja isso"), ('c',"ou isso"), ('d', 'd')], 'b', 0)
perguntaObj = []
perguntaObj.append(pergunta)
perguntas = json.dumps(([{"pergunta": perguntaObj[0].questionText, "respostas": perguntaObj[0].anwser, 'id': perguntaObj[0].id },{},{}]))

#dificuldade de jogo
dificuldade = -1

# Server socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

def findQuestion(id):
    for p in perguntaObj:
        if p.id == id:
            return p


print('Server UP')
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    try:
        if ('register' in json.loads(bytesAddressPair[0])):
            if(json.loads(bytesAddressPair[0])["register"] == True):
                jogadores.append(json.loads(bytesAddressPair[0])["client_id"])
                if(dificuldade == -1):
                    msgFromPlayer = json.dumps({'dificuldade':'Selecione a dificuldade', 'op': ['1) facil', '2) medio', '3) dificil']})
                    UDPServerSocket.sendto(bytes(msgFromPlayer, 'utf-8'), bytesAddressPair[1])
                elif len(jogadores) >= 2:
                    msgFromPlayer = json.dumps({'start':True})
                    UDPServerSocket.sendto(bytes(msgFromPlayer, 'utf-8'), bytesAddressPair[1])
                else:
                    msgFromPlayer = json.dumps({'wait':True})
                    UDPServerSocket.sendto(bytes(msgFromPlayer, 'utf-8'), bytesAddressPair[1])
        if ('registerDifficulty' in json.loads(bytesAddressPair[0])):
            dificuldade = int(json.loads(bytesAddressPair[0])["registerDifficulty"]) - 1
            if len(jogadores) >= 2:
                msgFromPlayer = json.dumps({'start':True})
            else:
                msgFromPlayer = json.dumps({'wait':True})
            UDPServerSocket.sendto(bytes(msgFromPlayer, 'utf-8'), bytesAddressPair[1])
        if ('wait' in json.loads(bytesAddressPair[0])):
            if len(jogadores) >= 2:
                msgFromPlayer = json.dumps({'start':True})
            else:
                msgFromPlayer = json.dumps({'wait':True})
            UDPServerSocket.sendto(bytes(msgFromPlayer, 'utf-8'), bytesAddressPair[1])
        if('resposta' in json.loads(bytesAddressPair[0])):
            pergunta = findQuestion(int(json.loads(bytesAddressPair[0])['id']))
            if pergunta.correctlyAnswer == json.loads(bytesAddressPair[0])['resposta']:
                msgFromPlayer = json.dumps({'recivePoints':10})
                UDPServerSocket.sendto(bytes(msgFromPlayer, 'utf-8'), bytesAddressPair[1])
            else:
                sendQuestion = json.dumps(json.loads(perguntas)[dificuldade])
                UDPServerSocket.sendto(bytes(sendQuestion, 'utf-8'), bytesAddressPair[1])
        if('continue' in json.loads(bytesAddressPair[0])):
            sendQuestion = json.dumps(json.loads(perguntas)[dificuldade])
            UDPServerSocket.sendto(bytes(sendQuestion, 'utf-8'), bytesAddressPair[1])
    except:
        sendQuestion = json.dumps(json.loads(perguntas)[dificuldade])
        UDPServerSocket.sendto(bytes(sendQuestion, 'utf-8'), bytesAddressPair[1])

