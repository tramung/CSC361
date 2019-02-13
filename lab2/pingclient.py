from socket import *
import sys
import time
BUFSIZE = 1024
host = str(sys.argv[1])
port = int(sys.argv[2])

try:
	clientSocket = socket(AF_INET, SOCK_DGRAM)
	print("Successfully created socket")
except socket.error, msg:
	print("Failed to create socket")
	sys.exit()
clientSocket.settimeout(1)


for i in range(10):
	sendTime = time.time()
	msg = "message " + str(i+1)
	clientSocket.sendto(msg, (host, port))
	try:
		data, server = clientSocket.recvfrom(BUFSIZE)
		recvTime = time.time()
		rtTime = recvTime - sendTime
		print("Received Message %s" + str(data))
		print("Round Trip Time is %s" + str(rtTime))

	except timeout:
		print("timeout")
