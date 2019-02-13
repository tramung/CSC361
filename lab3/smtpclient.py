from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
port = 25
mail_from = 'tramtung@uvic.ca'
mail_to = 'tramtung@uvic.ca'

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.gmail.com"

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port))


recv = clientSocket.recv(1024).decode()
if recv[:3] != '220':
	print('220 reply not received from server.')
else:
	print(recv)

# Send HELO command and print server response.
heloCommand = 'helo tramtung\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    
# Send MAIL FROM command and print server response.
mail_from_cmd = 'mail from:' + mail_from + '\r\n'
clientSocket.send(mail_from_cmd.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
	print('250 reply not received from server.')

# Send RCPT TO command and print server response. 
rcpt_to_cmd = 'rcpt to:' + mail_to + '\r\n'
clientSocket.send(rcpt_to_cmd.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
	print('250 reply not received from server.')

# Send DATA command and print server response. 
data_cmd = 'data\r\n'
clientSocket.send(data_cmd.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
	print('354 reply not received from server.')

# Send message data.
subject = 'subject: test email\r\n'
clientSocket.send(subject.encode())
clientSocket.send(msg.encode())


# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
	print('250 reply not received from server.')

# Send QUIT command and get server response.
quit_cmd = 'quit\r\n'
clientSocket.send(quit_cmd.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '221':
	print('221 reply not received from server. connection not closed.')