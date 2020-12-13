import socket
import sys
import json

mydata={"id": 20201234,"name":"Penando Torres","age":"21"}
sendData = json.dumps(mydata)

s = socket.socket()
print("Socket successfully created")

port = 8080

s.bind(('',port))
print("Socket binded to " +str(port))

s.listen(5)
print("Socket is listening")

while True:

	c,addr = s.accept()
	print("Got connecetion from" + str(addr))

	c.sendall(bytes(sendData,encoding = "utf-8"))
	buffer = c.recv(1024)
	print(buffer.decode('utf-8'))

c.close()
