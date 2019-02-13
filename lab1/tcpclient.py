import socket
import sys
BUFSIZE = 4096
PORT = 7777
#data given by client
IP = sys.argv[1]
FILENAME = sys.argv[3]
#create socket
try:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created.')
except socket.error, msg:
    print'Failed to create socket. Error ' + str(msg[0]) + ': ' + str(msg[1])
    sys.exit()
#connect to socket
clientSocket.connect((IP, PORT))
print('Connection Established...')
#send request
try:
    request = 'GET /' + str(FILENAME) +' HTTP/1.1\n\n'
    clientSocket.sendall(request)
except socket.error:
    print('Send Failed')
    sys.exit()
#receive data
data = clientSocket.recv(BUFSIZE)
print'data: ' + data
#close socket
clientSocket.close()
