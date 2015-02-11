"""sent motor test"""

import socket
import sys

HOST, PORT = "192.168.10.51",5000
print (HOST," ", PORT)
sock = socket.socket()

try:
	sock.connect((HOST,PORT))
	print ("connect")

except:
	print ("not connect")

else:
	sock.sendall(b'MOTOR,1,1,4,')	
	print("send")
	data = sock.recv(1024)	
	print("Received: ",data)
		
finally:
	sock.close()
	print ("close")
		
print ("stop")