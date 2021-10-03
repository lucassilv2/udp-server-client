import socket
import json
from question import question
# configuração do servidor
localIP = "127.0.0.1"
localPort = 20003
bufferSize = 1024

# array com jogadores
jogadores = []
# Perguntas em formato de objeto
perguntaObj = []
pergunta1  = question('Sabendo que uma intranet utiliza a infraestrutura de rede da empresa e fazendo uso das informações contidas no texto, considere que o computador de Paulo pode se comunicar com o computador servidor do Tribunal porque os recursos necessários estão fisicamente localizados em um raio de até 500 metros dentro do prédio do Tribunal, incluindo o computador de Paulo e o servidor. Isso significa que a rede utilizada é do tipo',[('a',"WAN."), ('b',"CAN."), ('c',"LAN."), ('d', 'MAN.'), ('e', 'ADSL.')], 'c', 0)
perguntaObj.append(pergunta1)
pergunta2  = question('Para conectar sua estação de trabalho a uma rede local de computadores controlada por um servidor de domínios, o usuário dessa rede deve informar uma senha e um[a]',[('a',"endereço de FTP válido para esse domínio."), ('b',"endereço MAC de rede registrado na máquina cliente."), ('c',"porta válida para a intranet desse domínio."), ('d', 'conta cadastrada e autorizada nesse domínio.'), ('e', 'certificação de navegação segura registrada na intranet.')], 'd', 1)
perguntaObj.append(pergunta2)
pergunta3  = question('Hoje, nas Redes Locais (LAN) cabeadas, o meio de transmissão mais utilizado é o',[('a',"Cabo de par trançado."), ('b',"Cabo de fibra óptica."), ('c',"Cabo coaxial."), ('d', 'Cabo Ethernet.'), ('e', 'Cabo fino 10BASE-T.')], 'a', 2)
perguntaObj.append(pergunta3)
pergunta4  = question('Dos equipamentos de rede abaixo, qual tem a função de escolher o melhor caminho para o envio da informação?',[('a','Switch'), ('b',"Roteador"), ('c',"Access Point"), ('d', 'Patch Panel'), ('e', 'Repetidor')], 'a', 3)
perguntaObj.append(pergunta4)
pergunta5  = question('Como é denominado o protocolo de configuração dinâmica de IP',[('a',"HTTP"), ('b',"FTP"), ('c',"DHCP"), ('d', 'DNS'), ('e', 'UDP')], 'c', 4)
perguntaObj.append(pergunta5)
# Perguntas em formato de json
perguntas = json.dumps(([{"pergunta": perguntaObj[0].questionText, "respostas": perguntaObj[0].anwser, 'id': perguntaObj[0].id },
                         {"pergunta": perguntaObj[1].questionText, "respostas": perguntaObj[1].anwser, 'id': perguntaObj[1].id },
                         {"pergunta": perguntaObj[2].questionText, "respostas": perguntaObj[2].anwser, 'id': perguntaObj[2].id },
                         {"pergunta": perguntaObj[3].questionText, "respostas": perguntaObj[3].anwser, 'id': perguntaObj[3].id },
                         {"pergunta": perguntaObj[4].questionText, "respostas": perguntaObj[4].anwser, 'id': perguntaObj[4].id },
                      ]))

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
        # recebeu register do client
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
                continue
        # recebeu registerDifficulty do client
        if ('registerDifficulty' in json.loads(bytesAddressPair[0])):
            dificuldade = int(json.loads(bytesAddressPair[0])["registerDifficulty"]) - 1
            if len(jogadores) >= 2:
                msgFromPlayer = json.dumps({'start':True})
            else:
                msgFromPlayer = json.dumps({'wait':True})
            UDPServerSocket.sendto(bytes(msgFromPlayer, 'utf-8'), bytesAddressPair[1])
            continue
        # recebeu wait do client
        if ('wait' in json.loads(bytesAddressPair[0])):
            if len(jogadores) >= 2:
                msgFromPlayer = json.dumps({'start':True})
            else:
                msgFromPlayer = json.dumps({'wait':True})
            UDPServerSocket.sendto(bytes(msgFromPlayer, 'utf-8'), bytesAddressPair[1])
            continue
        # recebeu resposta do client
        if('resposta' in json.loads(bytesAddressPair[0])):
            pergunta = findQuestion(int(json.loads(bytesAddressPair[0])['id']))
            if pergunta.correctlyAnswer == json.loads(bytesAddressPair[0])['resposta']:
                msgFromPlayer = json.dumps({'recivePoints':10})
                UDPServerSocket.sendto(bytes(msgFromPlayer, 'utf-8'), bytesAddressPair[1])
            else:
                sendQuestion = json.dumps(json.loads(perguntas)[dificuldade])
                UDPServerSocket.sendto(bytes(sendQuestion, 'utf-8'), bytesAddressPair[1])
                continue
        # recebeu continue do client
        if('continue' in json.loads(bytesAddressPair[0])):
            sendQuestion = json.dumps(json.loads(perguntas)[dificuldade])
            UDPServerSocket.sendto(bytes(sendQuestion, 'utf-8'), bytesAddressPair[1])
            continue
    except:
        sendQuestion = json.dumps(json.loads(perguntas)[dificuldade])
        UDPServerSocket.sendto(bytes(sendQuestion, 'utf-8'), bytesAddressPair[1])