import socket
import json

localIP = "127.0.0.1"
localPort = 20003
bufferSize = 1024

perguntas = json.dumps({"pergunta": "Sei lá qualquer coisa?", "respostas": ["sei la", "talvez seja isso", "ou isso"]})
bytesToSend =  bytes(perguntas, encoding="utf-8")


# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
 

# Listen for incoming datagrams

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

   

    # Sending a reply to client

    UDPServerSocket.sendto(bytesToSend, address)