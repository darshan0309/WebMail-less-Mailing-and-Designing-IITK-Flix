import cv2
import socket
import pickle
import struct


server_ip = "127.0.0.1"
server_port = 12345


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client_socket.connect((server_ip, server_port))
print(f"Connected to {server_ip}:{server_port}")

while True:
    data = client_socket.recv(4)
    message_size = struct.unpack("L", data)[0]
    data = b""
    while len(data) < message_size:
        packet = client_socket.recv(message_size - len(data))
        if not packet:
            break
        data += packet

    frame = pickle.loads(data)
    cv2.imshow("Received Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
client_socket.close()
cv2.destroyAllWindows()