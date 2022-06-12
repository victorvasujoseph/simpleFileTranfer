import socket

s = socket.socket()
host = socket.gethostname()
port = 8086
s.bind((host,port))
s.listen(1)
print("I'm waiting for incoming connection at" + " : " + host)
conn, addr = s.accept()
print(addr, "Connected...")

filename = input(str("Enter the filename you want to send"))
file = open(filename,'rb')
file_data = file.read()
conn.send(file_data)
print("File Sent")


