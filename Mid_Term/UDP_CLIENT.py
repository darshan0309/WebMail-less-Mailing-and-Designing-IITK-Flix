import socket
clientsock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg = input("Please eneter the lower case string")
clientsock.sendto(msg.encode(),('127.0.0.1',12345))
data ,addr = clientsock.recvfrom(2048)
print('Server returned')
print(data)
clientsock.close()  