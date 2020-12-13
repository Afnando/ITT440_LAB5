# first of all import the socket library  
import socket             
  
# next create a socket object  
s = socket.socket()       
print ("Berjaya buat socket") 
  
# reserve a port on your computer in our  
# case it is 12345 but it can be anything  
port = 8888 
  
# Next bind to the port  
# we have not typed any ip in the ip field  
# instead we have inputted an empty string  
# this makes the server listen to requests  
# coming from other computer on the network
s.bind(('',port))
print("Berjaya bind soket di port:" +str(port))

# put the socket into listening mode 
s.listen(5)
print("Soket tengah menunggu client!")

# a forever loop until we interrupt it or  
# an error occurs
while True:

	# Establish connection with client.
        c, addr=s.accept()
        print("Dapat capaian dari :" +str(addr))
	# send a thank you message to the client.  
        c.send(b'Terima Kasih!')
        buffer=c.recv(1024)
        print(buffer.decode('utf-8'))

c.close()

