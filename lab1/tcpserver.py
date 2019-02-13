import socket
import sys
BUFSIZE = 4096
PORT = 7777
#create socket
try:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created.')
except socket.error, msg:
    print'Failed to create socket. Error ' + str(msg[0]) + ': ' + str(msg[1])
    sys.exit()
#prepare a server socket
try:
    serverSocket.bind(('', PORT))
    print('Socket bind successful.')
except socket.error, msg:
    print'Bind failed. Error ' + str(msg[0]) + ': ' + str(msg[1])
    sys.exit()
serverSocket.listen(1)
while True:
    #establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print'Connected with ' + str(addr[0]) + ' ' + str(addr[1])
    try:
        message = connectionSocket.recv(BUFSIZE)
        print'message: ' + str(message)
        filename = message.split()[1]
        print'filename: ' + str(filename)
        f = open(filename[1:])
        print'f: ' + str(f)
        outputdata = f.read()
        print'outputdata' + str(outputdata)
        #send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        print'sent'

        #send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.sendall(outputdata[i].encode())
            #print'outputdata: ' + str(outputdata[i])
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        #send response message for file not found
        connectionSocket.send('404 Not Found')

        #close client socket
        connectionSocket.close()
#close server socket
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
