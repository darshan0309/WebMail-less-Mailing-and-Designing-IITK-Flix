import socket
clientsocket  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('127.0.0.1',12345))
sen = input("Enter the lower case string : ")
clientsocket.send(sen.encode())
modified = clientsocket.recv(1024)
print('From Server')
print(modified.decode())
clientsocket.close()