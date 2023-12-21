import socket 
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.bind(('127.0.0.1',12345))
serversocket.listen()
print("The server is ready to reiceve")
while True :
    data,addr = serversocket.accept()
    sen = data.recv(1024).decode()
    sen = sen.upper()
    data.send(sen.encode())
    data.close()