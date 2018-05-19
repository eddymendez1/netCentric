
# This is the library
from socket import *

# To what host data is doing and to what port
serverName = '10.0.0.70'
serverPort = 12000

# Addres family: AF_INET means underlying network is using IPv4
# second parameter SOCK_DGRAM means UDP socket
clientsocket = socket(AF_INET, SOCK_DGRAM)

#type into command line
message = raw_input('Input lowercase sentence: \n')

#convert to bytes since we need to stream bytes
# send to server from client 
clientsocket.sendto(message.encode(), (serverName, serverPort))

#modified message is the packets data
# server address is the IP and port number done 
# OS takes care of assigning a port to client process
# buffer size 2048 bytes 
modifiedMessage, serverAddress = clientsocket.recvfrom(2048)
print (modifiedMessage.decode())
