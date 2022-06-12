from ast import Str
import socket

s = socket.socket()
host = raw_input ("Enter the host address : ")
port = 8086
s.connect((host,port))
print("connected....")

filename = raw_input("Enter a filename for incoming file :")

file = open(filename,'wb')
file_data = s.recv(1024)
while file_data:
    file.write(file_data)
    file_data = s.recv(1024)
file.close()

print("File received !!")
