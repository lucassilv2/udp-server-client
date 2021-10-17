import socket
import json
import threading
from question import question
from datetime import datetime
import time
# configuração do servidor
localIP = "127.0.0.1"
localPort = 20003
bufferSize = 1024
# Perguntas em formato de objeto

class server():
    

    def __init__(self):
        self.host = localIP    
        self.port = localPort  
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.socket_lock = threading.Lock()
        self.socket.bind((localIP, localPort))
        self.jogadores = []
        self.primeiroJogadorAcabou = 0
        self.dificuldade = -1
        self.difficultyChange = True
        self.perguntaObj1 = []
        pergunta1  = question('Sabendo que uma intranet utiliza a infraestrutura de rede da empresa e fazendo uso das informações contidas no texto, considere que o computador de Paulo pode se comunicar com o computador servidor do Tribunal porque os recursos necessários estão fisicamente localizados em um raio de até 500 metros dentro do prédio do Tribunal, incluindo o computador de Paulo e o servidor. Isso significa que a rede utilizada é do tipo',[('a',"WAN."), ('b',"CAN."), ('c',"LAN.")], 'c', 0)
        self.perguntaObj1.append(pergunta1)
        pergunta2  = question('Para conectar sua estação de trabalho a uma rede local de computadores controlada por um servidor de domínios, o usuário dessa rede deve informar uma senha e um[a]',[('a',"endereço de FTP válido para esse domínio."), ('b',"endereço MAC de rede registrado na máquina cliente."), ('c', 'conta cadastrada e autorizada nesse domínio.')], 'c', 1)
        self.perguntaObj1.append(pergunta2)
        pergunta3  = question('Hoje, nas Redes Locais (LAN) cabeadas, o meio de transmissão mais utilizado é o',[('a',"Cabo de par trançado."), ('b',"Cabo de fibra óptica."), ('c',"Cabo coaxial.")], 'a', 2)
        self.perguntaObj1.append(pergunta3)
        pergunta4  = question('Dos equipamentos de rede abaixo, qual tem a função de escolher o melhor caminho para o envio da informação?',[('a','Switch'), ('b',"Roteador"), ('c',"Access Point")], 'a', 3)
        self.perguntaObj1.append(pergunta4)
        pergunta5  = question('Como é denominado o protocolo de configuração dinâmica de IP',[('a',"HTTP"), ('b',"FTP"), ('c',"DHCP")], 'c', 4)
        self.perguntaObj1.append(pergunta5)
        self.perguntaObj2 = []
        pergunta1  = question('Sabendo que uma intranet utiliza a infraestrutura de rede da empresa e fazendo uso das informações contidas no texto, considere que o computador de Paulo pode se comunicar com o computador servidor do Tribunal porque os recursos necessários estão fisicamente localizados em um raio de até 500 metros dentro do prédio do Tribunal, incluindo o computador de Paulo e o servidor. Isso significa que a rede utilizada é do tipo',[('a',"WAN."), ('b',"CAN."), ('c',"LAN."), ('d', 'MAN.')], 'c', 0)
        self.perguntaObj2.append(pergunta1)
        pergunta2  = question('Para conectar sua estação de trabalho a uma rede local de computadores controlada por um servidor de domínios, o usuário dessa rede deve informar uma senha e um[a]',[('a',"endereço de FTP válido para esse domínio."), ('b',"endereço MAC de rede registrado na máquina cliente."), ('c',"porta válida para a intranet desse domínio."), ('d', 'conta cadastrada e autorizada nesse domínio.')], 'd', 1)
        self.perguntaObj2.append(pergunta2)
        pergunta3  = question('Hoje, nas Redes Locais (LAN) cabeadas, o meio de transmissão mais utilizado é o',[('a',"Cabo de par trançado."), ('b',"Cabo de fibra óptica."), ('c',"Cabo coaxial."), ('d', 'Cabo Ethernet.')], 'a', 2)
        self.perguntaObj2.append(pergunta3)
        pergunta4  = question('Dos equipamentos de rede abaixo, qual tem a função de escolher o melhor caminho para o envio da informação?',[('a','Switch'), ('b',"Roteador"), ('c',"Access Point"), ('d', 'Patch Panel')], 'a', 3)
        self.perguntaObj2.append(pergunta4)
        pergunta5  = question('Como é denominado o protocolo de configuração dinâmica de IP',[('a',"HTTP"), ('b',"FTP"), ('c',"DHCP"), ('d', 'DNS')], 'c', 4)
        self.perguntaObj2.append(pergunta5)
        self.perguntaObj3 = []
        pergunta1  = question('Sabendo que uma intranet utiliza a infraestrutura de rede da empresa e fazendo uso das informações contidas no texto, considere que o computador de Paulo pode se comunicar com o computador servidor do Tribunal porque os recursos necessários estão fisicamente localizados em um raio de até 500 metros dentro do prédio do Tribunal, incluindo o computador de Paulo e o servidor. Isso significa que a rede utilizada é do tipo',[('a',"WAN."), ('b',"CAN."), ('c',"LAN."), ('d', 'MAN.'), ('e', 'ADSL.')], 'c', 0)
        self.perguntaObj3.append(pergunta1)
        pergunta2  = question('Para conectar sua estação de trabalho a uma rede local de computadores controlada por um servidor de domínios, o usuário dessa rede deve informar uma senha e um[a]',[('a',"endereço de FTP válido para esse domínio."), ('b',"endereço MAC de rede registrado na máquina cliente."), ('c',"porta válida para a intranet desse domínio."), ('d', 'conta cadastrada e autorizada nesse domínio.'), ('e', 'certificação de navegação segura registrada na intranet.')], 'd', 1)
        self.perguntaObj3.append(pergunta2)
        pergunta3  = question('Hoje, nas Redes Locais (LAN) cabeadas, o meio de transmissão mais utilizado é o',[('a',"Cabo de par trançado."), ('b',"Cabo de fibra óptica."), ('c',"Cabo coaxial."), ('d', 'Cabo Ethernet.'), ('e', 'Cabo fino 10BASE-T.')], 'a', 2)
        self.perguntaObj3.append(pergunta3)
        pergunta4  = question('Dos equipamentos de rede abaixo, qual tem a função de escolher o melhor caminho para o envio da informação?',[('a','Switch'), ('b',"Roteador"), ('c',"Access Point"), ('d', 'Patch Panel'), ('e', 'Repetidor')], 'a', 3)
        self.perguntaObj3.append(pergunta4)
        pergunta5  = question('Como é denominado o protocolo de configuração dinâmica de IP',[('a',"HTTP"), ('b',"FTP"), ('c',"DHCP"), ('d', 'DNS'), ('e', 'UDP')], 'c', 4)
        self.perguntaObj3.append(pergunta5)
        # Perguntas em formato de json
        self.perguntas1 = json.dumps(([
                         {"pergunta": self.perguntaObj1[0].questionText, "respostas": self.perguntaObj1[0].anwser, 'id': self.perguntaObj1[0].id },
                         {"pergunta": self.perguntaObj1[1].questionText, "respostas": self.perguntaObj1[1].anwser, 'id': self.perguntaObj1[1].id },
                         {"pergunta": self.perguntaObj1[2].questionText, "respostas": self.perguntaObj1[2].anwser, 'id': self.perguntaObj1[2].id },
                         {"pergunta": self.perguntaObj1[3].questionText, "respostas": self.perguntaObj1[3].anwser, 'id': self.perguntaObj1[3].id },
                         {"pergunta": self.perguntaObj1[4].questionText, "respostas": self.perguntaObj1[4].anwser, 'id': self.perguntaObj1[4].id },
                      ]))
        self.perguntas2 = json.dumps(([
                         {"pergunta": self.perguntaObj2[0].questionText, "respostas": self.perguntaObj2[0].anwser, 'id': self.perguntaObj2[0].id },
                         {"pergunta": self.perguntaObj2[1].questionText, "respostas": self.perguntaObj2[1].anwser, 'id': self.perguntaObj2[1].id },
                         {"pergunta": self.perguntaObj2[2].questionText, "respostas": self.perguntaObj2[2].anwser, 'id': self.perguntaObj2[2].id },
                         {"pergunta": self.perguntaObj2[3].questionText, "respostas": self.perguntaObj2[3].anwser, 'id': self.perguntaObj2[3].id },
                         {"pergunta": self.perguntaObj2[4].questionText, "respostas": self.perguntaObj2[4].anwser, 'id': self.perguntaObj2[4].id },
                      ]))
        self.perguntas3 = json.dumps(([
                         {"pergunta": self.perguntaObj3[0].questionText, "respostas": self.perguntaObj3[0].anwser, 'id': self.perguntaObj3[0].id },
                         {"pergunta": self.perguntaObj3[1].questionText, "respostas": self.perguntaObj3[1].anwser, 'id': self.perguntaObj3[1].id },
                         {"pergunta": self.perguntaObj3[2].questionText, "respostas": self.perguntaObj3[2].anwser, 'id': self.perguntaObj3[2].id },
                         {"pergunta": self.perguntaObj3[3].questionText, "respostas": self.perguntaObj3[3].anwser, 'id': self.perguntaObj3[3].id },
                         {"pergunta": self.perguntaObj3[4].questionText, "respostas": self.perguntaObj3[4].anwser, 'id': self.perguntaObj3[4].id },
                      ]))
    
    def initialize_player(self):
         # array com jogadores
        self.jogadores = []
         # alguem terminou o jogo
        self.primeiroJogadorAcabou = 0
    
    def initialize_difficulty(self):
        #dificuldade de jogo
        self.dificuldade = -1
        self.difficultyChange = True

    def results(self ,myID):
        r = []
        for i, jogador in enumerate(self.jogadores):
            if(jogador[0] == myID):
                r.append('My - '+str(jogador[1][0])+" pontos")
            else:
                r.append('Jogador-'+str(i+1)+' - '+str(jogador[1][0])+" pontos")
        return r

    def findQuestion(self, id, perguntaObj):
        for p in perguntaObj:
            if p.id == id:
                return p

    def retornaQuestions(self, dificuldade):
        if dificuldade == 1:
            return self.perguntas1
        elif dificuldade == 2:
            return self.perguntas2
        else:
            return self.perguntas3

    def registraCliente(self,data, client_address):
        if(json.loads(data)["register"] == True):
            if self.dificuldade == 1:
                self.jogadores.append((client_address, [0, json.loads(self.perguntas1)]))
            if self.dificuldade == 2:
                self.jogadores.append((client_address, [0, json.loads(self.perguntas2)]))
            if self.dificuldade == 3:
                self.jogadores.append((client_address, [0, json.loads(self.perguntas3)]))
            if(self.dificuldade == -1):
                msgFromPlayer = json.dumps({'setDifficulty':'Selecione a dificuldade', 'op': ['1) facil', '2) medio', '3) dificil']})
                with self.socket_lock:
                    self.socket.sendto(bytes(msgFromPlayer, 'utf-8'), client_address)
              
            elif len(self.jogadores) >= 2:
                msgFromPlayer = json.dumps({'start':True})
                with self.socket_lock:
                    self.socket.sendto(bytes(msgFromPlayer, 'utf-8'), client_address)
            else:
                msgFromPlayer = json.dumps({'wait':True})
                with self.socket_lock:
                    self.socket.sendto(bytes(msgFromPlayer, 'utf-8'), client_address)
        

    def  recebeContinue(self, data, client_address):
        self.jogadores = dict(self.jogadores)
        if len(self.jogadores[client_address][1]) == 0:
            self.jogadores = [(k, v) for k, v in self.jogadores.items()]
            msgFromPlayer = json.dumps({'yourGameEnd':True})
            if self.primeiroJogadorAcabou == 0:
                self.primeiroJogadorAcabou = datetime.now()
            elif (datetime.now() - self.primeiroJogadorAcabou).seconds > 10:
                msgFromPlayer = json.dumps({'end':True})
            with self.socket_lock:
                self.socket.sendto(bytes(msgFromPlayer, 'utf-8'), client_address)
              
        else:
            sendQuestion = json.dumps(self.jogadores[client_address][1][0])
            #self.jogadores = dict(self.jogadores)
            self.jogadores[client_address][1].pop(0)
            #self.jogadores = [(k, v) for k, v in self.jogadores.items()]
            with self.socket_lock:
                self.socket.sendto(bytes(sendQuestion, 'utf-8'), client_address)
              

    def registraDificuldade(self, data, client_address):
        if self.difficultyChange:
            self.dificuldade = int(json.loads(data)["registerDifficulty"])
            self.difficultyChange = False
        self.jogadores.append((client_address, [0, json.loads(self.retornaQuestions(self.dificuldade))]))
        if len(self.jogadores) >= 2:
            msgFromPlayer = json.dumps({'start':True})
        else:
            msgFromPlayer = json.dumps({'wait':True})
            with self.socket_lock:
                self.socket.sendto(bytes(msgFromPlayer, 'utf-8'), client_address)
    
    def enviaWaitStart(self, data, client_address):
        if len(self.jogadores) >= 2:
            msgFromPlayer = json.dumps({'start':True})
        else:
            msgFromPlayer = json.dumps({'wait':True})
        with self.socket_lock:
            self.socket.sendto(bytes(msgFromPlayer, 'utf-8'), client_address)

    def recebeRespostaPergunta(self, data, client_address):
        if(self.dificuldade == 1):
            pergunta = self.findQuestion(int(json.loads(data)['id']), self.perguntaObj1)
        elif self.dificuldade == 2:
            pergunta = self.findQuestion(int(json.loads(data)['id']), self.perguntaObj2)
        else:
            pergunta = self.findQuestion(int(json.loads(data)['id']), self.perguntaObj3)
        if pergunta.correctlyAnswer == json.loads(data)['response']:
            self.jogadores = dict(self.jogadores)
            self.jogadores[client_address][0] = int(self.jogadores[client_address][0]) + 10
            self.jogadores = [(k, v) for k, v in self.jogadores.items()]
            msgFromPlayer = json.dumps({'recivePoints':10})
            with self.socket_lock:
                self.socket.sendto(bytes(msgFromPlayer, 'utf-8'), client_address)
        else:
            self.jogadores = dict(self.jogadores)
            sendQuestion = json.dumps(self.jogadores[client_address][1][0])
            self.jogadores[client_address][1].pop(0)
            self.jogadores = [(k, v) for k, v in self.jogadores.items()]
            with self.socket_lock:
                self.socket.sendto(bytes(sendQuestion, 'utf-8'), client_address)
        
    def runServer(self):
        while(True):
            data, client_address = self.socket.recvfrom(bufferSize)
            try:
                # recebeu register do client
                if ('register' in json.loads(data)):
                    c_thread = threading.Thread(target = self.registraCliente,
                                            args = (data, client_address))
                    c_thread.daemon = True
                    c_thread.start()
                    time.sleep(2)
                    continue
                # recebeu registerDifficulty do client
                if ('registerDifficulty' in json.loads(data)):
                    # so pode ser alterada uma vez
                    c_thread = threading.Thread(target = self.registraDificuldade,
                                            args = (data, client_address))
                    c_thread.daemon = True
                    c_thread.start()
                    continue
                # recebeu wait do client
                if ('wait' in json.loads(data)):
                    c_thread = threading.Thread(target = self.enviaWaitStart,
                                            args = (data, client_address))
                    c_thread.daemon = True
                    c_thread.start()
                    continue
                # recebeu resposta de uma pergunta do client
                if('response' in json.loads(data)):
                    c_thread = threading.Thread(target = self.recebeRespostaPergunta,
                                            args = (data, client_address))
                    c_thread.daemon = True
                    c_thread.start()
                    continue
                if('results' in json.loads(data)):
                    msgFromPlayer = json.dumps({'finish':self.results(client_address)})
                    self.socket.sendto(bytes(msgFromPlayer, 'utf-8'), client_address)
                    continue
                # recebeu continue do client
                # significa que o cliente acabou de responder suas perguntas porem ainda os outros ainda tem tempo de responder
                # se ele não terminou de responder ele recebe sua proxima pergunta
                if('continue' in json.loads(data)):
                    c_thread = threading.Thread(target = self.recebeContinue,
                                            args = (data, client_address))
                    c_thread.daemon = True
                    c_thread.start()
                    continue
            except:
                self.jogadores = dict(self.jogadores)
                if len(self.jogadores[client_address][1]) == 0:
                    msgFromPlayer = json.dumps({'yourGameEnd':True})
                    with self.socket_lock:
                        self.socket.sendto(bytes(msgFromPlayer, 'utf-8'), client_address)
                else:
                    sendQuestion = json.dumps(self.jogadores[client_address][1][0])
                    with self.socket_lock:
                        self.socket.sendto(bytes(sendQuestion, 'utf-8'), client_address)

def main():

    udp_server = server()
    print('Server UP')
    udp_server.runServer()

if __name__ == '__main__':
    main()
