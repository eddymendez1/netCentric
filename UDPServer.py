from socket import *
serverPort = 12000
serverSocket =  socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to recieve: \n"
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    print "Sending Modified Message: "
    print modifiedMessage
    print "\n"
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
