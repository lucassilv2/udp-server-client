import socket
import random
from client import client
import json
import time



# Codigo do cliente
cl = client(random.randint(100000,999999), 0)

# Condição para registrar o jogador
registerClient = True

# Socket para cliente
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 20003)
bufferSize = 1024

# Condição para iniciar o jogo
start = False

# variavel auxiliar para nao ficar repetindo mensagem de esperando jogadores
noLoopWait = True

while registerClient:
    # aperte s para iniciar o jogo
    value = input("Press 's' for start\n")
    if(value == 's'):
        msgFromServer = json.dumps({"register":True, "client_id":cl.id})
        bytesToSend = bytes(msgFromServer, encoding="utf-8")
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        registerClient = False


while True:
    # Recebendo messagem do servidor
    msgToServer = UDPClientSocket.recvfrom(bufferSize)

    # se for primeiro jogador seta a dificuldade
    if("setDifficulty" in json.loads(msgToServer[0])):
        waitValidResponse = True
        print('\n')
        print(json.loads(msgToServer[0])["setDifficulty"])
        for msg in json.loads(msgToServer[0])['op'] :
            print(msg)
        while waitValidResponse:
            value = input("Sua resposta:\n")
            if(value == '1' or value == '2' or value == '3' ):
                waitValidResponse = False
                msgFromServer = json.dumps({'registerDifficulty':value})
                UDPClientSocket.sendto(bytes(msgFromServer, 'utf-8'), serverAddressPort)
        continue
    # recebe o start do servidor e torna client elegivel de responder perguntas
    if('start' in json.loads(msgToServer[0])):
        if json.loads(msgToServer[0])['start'] == True:
            start = True
            msgFromServer = json.dumps({'continue':'ok'})
            UDPClientSocket.sendto(bytes(msgFromServer, 'utf-8'), serverAddressPort)
        continue
    # fica esperando ter pelo menos + 1 jogador para totalizar o minimo de 2
    if('wait' in json.loads(msgToServer[0])):
        if json.loads(msgToServer[0])['wait'] == True:
            if noLoopWait:
                print('\n')
                print('Esperando jogadores...')
                noLoopWait = False
            msgFromServer = json.dumps({'wait':'ok'})
            UDPClientSocket.sendto(bytes(msgFromServer, 'utf-8'), serverAddressPort)
        continue
    if('recivePoints' in json.loads(msgToServer[0])):
        cl.points = cl.points + int(json.loads(msgToServer[0])['recivePoints'])
        print('\n')
        print('Você tem '+str(cl.points)+' pontos')

        msgFromServer = json.dumps({'continue':'ok'})
        UDPClientSocket.sendto(bytes(msgFromServer, 'utf-8'), serverAddressPort)
        continue
    if('yourGameEnd' in json.loads(msgToServer[0])):
        print("Você finalizou suas questões aguarde os outros jogadores.")
        msgFromServer = json.dumps({'continue':'ok'})
        time.sleep(5)
        UDPClientSocket.sendto(bytes(msgFromServer, 'utf-8'), serverAddressPort)
        continue
    if('end' in json.loads(msgToServer[0])):
        msgFromServer = json.dumps({'results':'ok'})
        UDPClientSocket.sendto(bytes(msgFromServer, 'utf-8'), serverAddressPort)
        continue
    if('finish' in json.loads(msgToServer[0])):
        print('Resultados:')
        for msg in json.loads(msgToServer[0])['finish'] :
            print(msg)
        continue
    # se servidor ja estiver preparado para enviar pergunta start sera verdadeiro
    if(start):
        msgFromServer = json.dumps({'continue':'ok'})
        UDPClientSocket.sendto(bytes(msgFromServer, 'utf-8'), serverAddressPort)
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        print('\n')
        print("Pergunta: ")
        print(json.loads(msgToServer[0])['pergunta'])
        print("Respostas: ")
        waitValidResponse = True
        for msg in json.loads(msgToServer[0])['respostas'] :
            print(msg[0]+') '+msg[1])
        while waitValidResponse:
            value = input("Sua resposta:\n")
            if(value == 'a' or value == 'b' or value == 'c' or value == 'd' or value == 'e' ):
                waitValidResponse = False
        id = int(json.loads(msgToServer[0])['id'])
        UDPClientSocket.sendto(bytes(json.dumps({'response':value , 'id': id}), 'utf-8'), serverAddressPort)