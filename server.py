import socket
import json
from question import question
from datetime import datetime
# configuração do servidor
localIP = "127.0.0.1"
localPort = 20003
bufferSize = 1024

# array com jogadores
jogadores = []
primeiroJogadorAcabou = 0
# Perguntas em formato de objeto
perguntaObj1 = []
pergunta1  = question('Sabendo que uma intranet utiliza a infraestrutura de rede da empresa e fazendo uso das informações contidas no texto, considere que o computador de Paulo pode se comunicar com o computador servidor do Tribunal porque os recursos necessários estão fisicamente localizados em um raio de até 500 metros dentro do prédio do Tribunal, incluindo o computador de Paulo e o servidor. Isso significa que a rede utilizada é do tipo',[('a',"WAN."), ('b',"CAN."), ('c',"LAN.")], 'c', 0)
perguntaObj1.append(pergunta1)
pergunta2  = question('Para conectar sua estação de trabalho a uma rede local de computadores controlada por um servidor de domínios, o usuário dessa rede deve informar uma senha e um[a]',[('a',"endereço de FTP válido para esse domínio."), ('b',"endereço MAC de rede registrado na máquina cliente."), ('c', 'conta cadastrada e autorizada nesse domínio.')], 'c', 1)
perguntaObj1.append(pergunta2)
pergunta3  = question('Hoje, nas Redes Locais (LAN) cabeadas, o meio de transmissão mais utilizado é o',[('a',"Cabo de par trançado."), ('b',"Cabo de fibra óptica."), ('c',"Cabo coaxial.")], 'a', 2)
perguntaObj1.append(pergunta3)
pergunta4  = question('Dos equipamentos de rede abaixo, qual tem a função de escolher o melhor caminho para o envio da informação?',[('a','Switch'), ('b',"Roteador"), ('c',"Access Point")], 'a', 3)
perguntaObj1.append(pergunta4)
pergunta5  = question('Como é denominado o protocolo de configuração dinâmica de IP',[('a',"HTTP"), ('b',"FTP"), ('c',"DHCP")], 'c', 4)
perguntaObj1.append(pergunta5)

perguntaObj2 = []
pergunta1  = question('Sabendo que uma intranet utiliza a infraestrutura de rede da empresa e fazendo uso das informações contidas no texto, considere que o computador de Paulo pode se comunicar com o computador servidor do Tribunal porque os recursos necessários estão fisicamente localizados em um raio de até 500 metros dentro do prédio do Tribunal, incluindo o computador de Paulo e o servidor. Isso significa que a rede utilizada é do tipo',[('a',"WAN."), ('b',"CAN."), ('c',"LAN."), ('d', 'MAN.')], 'c', 0)
perguntaObj2.append(pergunta1)
pergunta2  = question('Para conectar sua estação de trabalho a uma rede local de computadores controlada por um servidor de domínios, o usuário dessa rede deve informar uma senha e um[a]',[('a',"endereço de FTP válido para esse domínio."), ('b',"endereço MAC de rede registrado na máquina cliente."), ('c',"porta válida para a intranet desse domínio."), ('d', 'conta cadastrada e autorizada nesse domínio.')], 'd', 1)
perguntaObj2.append(pergunta2)
pergunta3  = question('Hoje, nas Redes Locais (LAN) cabeadas, o meio de transmissão mais utilizado é o',[('a',"Cabo de par trançado."), ('b',"Cabo de fibra óptica."), ('c',"Cabo coaxial."), ('d', 'Cabo Ethernet.')], 'a', 2)
perguntaObj2.append(pergunta3)
pergunta4  = question('Dos equipamentos de rede abaixo, qual tem a função de escolher o melhor caminho para o envio da informação?',[('a','Switch'), ('b',"Roteador"), ('c',"Access Point"), ('d', 'Patch Panel')], 'a', 3)
perguntaObj2.append(pergunta4)
pergunta5  = question('Como é denominado o protocolo de configuração dinâmica de IP',[('a',"HTTP"), ('b',"FTP"), ('c',"DHCP"), ('d', 'DNS')], 'c', 4)
perguntaObj2.append(pergunta5)

perguntaObj3 = []
pergunta1  = question('Sabendo que uma intranet utiliza a infraestrutura de rede da empresa e fazendo uso das informações contidas no texto, considere que o computador de Paulo pode se comunicar com o computador servidor do Tribunal porque os recursos necessários estão fisicamente localizados em um raio de até 500 metros dentro do prédio do Tribunal, incluindo o computador de Paulo e o servidor. Isso significa que a rede utilizada é do tipo',[('a',"WAN."), ('b',"CAN."), ('c',"LAN."), ('d', 'MAN.'), ('e', 'ADSL.')], 'c', 0)
perguntaObj3.append(pergunta1)
pergunta2  = question('Para conectar sua estação de trabalho a uma rede local de computadores controlada por um servidor de domínios, o usuário dessa rede deve informar uma senha e um[a]',[('a',"endereço de FTP válido para esse domínio."), ('b',"endereço MAC de rede registrado na máquina cliente."), ('c',"porta válida para a intranet desse domínio."), ('d', 'conta cadastrada e autorizada nesse domínio.'), ('e', 'certificação de navegação segura registrada na intranet.')], 'd', 1)
perguntaObj3.append(pergunta2)
pergunta3  = question('Hoje, nas Redes Locais (LAN) cabeadas, o meio de transmissão mais utilizado é o',[('a',"Cabo de par trançado."), ('b',"Cabo de fibra óptica."), ('c',"Cabo coaxial."), ('d', 'Cabo Ethernet.'), ('e', 'Cabo fino 10BASE-T.')], 'a', 2)
perguntaObj3.append(pergunta3)
pergunta4  = question('Dos equipamentos de rede abaixo, qual tem a função de escolher o melhor caminho para o envio da informação?',[('a','Switch'), ('b',"Roteador"), ('c',"Access Point"), ('d', 'Patch Panel'), ('e', 'Repetidor')], 'a', 3)
perguntaObj3.append(pergunta4)
pergunta5  = question('Como é denominado o protocolo de configuração dinâmica de IP',[('a',"HTTP"), ('b',"FTP"), ('c',"DHCP"), ('d', 'DNS'), ('e', 'UDP')], 'c', 4)
perguntaObj3.append(pergunta5)
# Perguntas em formato de json
perguntas1 = json.dumps(([
                         {"pergunta": perguntaObj1[0].questionText, "respostas": perguntaObj1[0].anwser, 'id': perguntaObj1[0].id },
                         {"pergunta": perguntaObj1[1].questionText, "respostas": perguntaObj1[1].anwser, 'id': perguntaObj1[1].id },
                         {"pergunta": perguntaObj1[2].questionText, "respostas": perguntaObj1[2].anwser, 'id': perguntaObj1[2].id },
                         {"pergunta": perguntaObj1[3].questionText, "respostas": perguntaObj1[3].anwser, 'id': perguntaObj1[3].id },
                         {"pergunta": perguntaObj1[4].questionText, "respostas": perguntaObj1[4].anwser, 'id': perguntaObj1[4].id },
                      ]))
perguntas2 = json.dumps(([
                         {"pergunta": perguntaObj2[0].questionText, "respostas": perguntaObj2[0].anwser, 'id': perguntaObj2[0].id },
                         {"pergunta": perguntaObj2[1].questionText, "respostas": perguntaObj2[1].anwser, 'id': perguntaObj2[1].id },
                         {"pergunta": perguntaObj2[2].questionText, "respostas": perguntaObj2[2].anwser, 'id': perguntaObj2[2].id },
                         {"pergunta": perguntaObj2[3].questionText, "respostas": perguntaObj2[3].anwser, 'id': perguntaObj2[3].id },
                         {"pergunta": perguntaObj2[4].questionText, "respostas": perguntaObj2[4].anwser, 'id': perguntaObj2[4].id },
                      ]))
perguntas3 = json.dumps(([
                         {"pergunta": perguntaObj2[0].questionText, "respostas": perguntaObj3[0].anwser, 'id': perguntaObj3[0].id },
                         {"pergunta": perguntaObj2[1].questionText, "respostas": perguntaObj3[1].anwser, 'id': perguntaObj3[1].id },
                         {"pergunta": perguntaObj2[2].questionText, "respostas": perguntaObj3[2].anwser, 'id': perguntaObj3[2].id },
                         {"pergunta": perguntaObj2[3].questionText, "respostas": perguntaObj3[3].anwser, 'id': perguntaObj3[3].id },
                         {"pergunta": perguntaObj2[4].questionText, "respostas": perguntaObj3[4].anwser, 'id': perguntaObj3[4].id },
                      ]))
#dificuldade de jogo
dificuldade = -1
difficultyChange = True
# Server socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

def findQuestion(id, perguntaObj):
    for p in perguntaObj:
        if p.id == id:
            return p

def retornaQuestions(dificuldade):
    if dificuldade == 1:
        return perguntas1
    elif dificuldade == 2:
        return perguntas2
    else:
        return perguntas3

print('Server UP')
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    try:
        # recebeu register do client
        if ('register' in json.loads(bytesAddressPair[0])):
            if(json.loads(bytesAddressPair[0])["register"] == True):
                if dificuldade == 1:
                    jogadores.append((bytesAddressPair[1], [0, json.loads(perguntas1)]))
                if dificuldade == 2:
                    jogadores.append((bytesAddressPair[1], [0, json.loads(perguntas2)]))
                if dificuldade == 3:
                    jogadores.append((bytesAddressPair[1], [0, json.loads(perguntas3)]))
                if(dificuldade == -1):
                    msgFromPlayer = json.dumps({'setDifficulty':'Selecione a dificuldade', 'op': ['1) facil', '2) medio', '3) dificil']})
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
            # so pode ser alterada uma vez
            if difficultyChange:
                dificuldade = int(json.loads(bytesAddressPair[0])["registerDifficulty"])
                difficultyChange = False
            jogadores.append((bytesAddressPair[1], [0, json.loads(retornaQuestions(dificuldade))]))
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
        if('response' in json.loads(bytesAddressPair[0])):
            pergunta = findQuestion(int(json.loads(bytesAddressPair[0])['id']))
            if pergunta.correctlyAnswer == json.loads(bytesAddressPair[0])['response']:
                jogadores = dict(jogadores)
                jogadores[bytesAddressPair[1]][0] = int(jogadores[bytesAddressPair[1]][0]) + 10
                jogadores = [(k, v) for k, v in jogadores.items()]
                msgFromPlayer = json.dumps({'recivePoints':10})
                UDPServerSocket.sendto(bytes(msgFromPlayer, 'utf-8'), bytesAddressPair[1])
            else:
                jogadores = dict(jogadores)
                sendQuestion = json.dumps(jogadores[bytesAddressPair[1]][1][0])
                jogadores[bytesAddressPair[1]][1].pop(0)
                jogadores = [(k, v) for k, v in jogadores.items()]
                UDPServerSocket.sendto(bytes(sendQuestion, 'utf-8'), bytesAddressPair[1])
            continue
        if('results' in json.loads(bytesAddressPair[0])):
            msgFromPlayer = json.dumps({'finish':['vai ter resultados aqui','nesse formato']})
            UDPServerSocket.sendto(bytes(msgFromPlayer, 'utf-8'), bytesAddressPair[1])
            continue
        # recebeu continue do client
        if('continue' in json.loads(bytesAddressPair[0])):
            jogadores = dict(jogadores)
            if len(jogadores[bytesAddressPair[1]][1]) == 0:
                jogadores = [(k, v) for k, v in jogadores.items()]
                msgFromPlayer = json.dumps({'yourGameEnd':True})
                if primeiroJogadorAcabou == 0:
                    primeiroJogadorAcabou = datetime.now()
                elif (datetime.now() - primeiroJogadorAcabou).seconds > 10:
                    msgFromPlayer = json.dumps({'end':True})
                UDPServerSocket.sendto(bytes(msgFromPlayer, 'utf-8'), bytesAddressPair[1])
            else:
                sendQuestion = json.dumps(jogadores[bytesAddressPair[1]][1][0])
                jogadores = dict(jogadores)
               
                jogadores[bytesAddressPair[1]][1].pop(0)
                jogadores = [(k, v) for k, v in jogadores.items()]
                UDPServerSocket.sendto(bytes(sendQuestion, 'utf-8'), bytesAddressPair[1])
            continue
    except:
        jogadores = dict(jogadores)
        if len(jogadores[bytesAddressPair[1]][1]) == 0:
            msgFromPlayer = json.dumps({'yourGameEnd':True})
            UDPServerSocket.sendto(bytes(msgFromPlayer, 'utf-8'), bytesAddressPair[1])
        else:
            sendQuestion = json.dumps(jogadores[bytesAddressPair[1]][1][0])
            UDPServerSocket.sendto(bytes(sendQuestion, 'utf-8'), bytesAddressPair[1])
        jogadores = [(k, v) for k, v in jogadores.items()]
           