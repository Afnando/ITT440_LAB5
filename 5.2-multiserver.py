#import socket
import socket
import os
from _thread import *

#create a connection
ServerSocket = socket.socket()
host = '192.168.120.11'
port = 8889
ThreadCount = 0

#bind the host and port
#return error when conncetion fail
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)

#handle multiple client
def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server\n'))
    while True:
        data = connection.recv(2048)
        reply = 'Server Says: ' + data.decode('utf-8')
        if not data:
            break
        print('Client:' + data.decode('utf-8'))
        connection.sendall(str.encode(reply))
    connection.close()

#accept and keep alive client connection
while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()
