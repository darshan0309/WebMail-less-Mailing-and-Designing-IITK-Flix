import cv2
import socket
import pickle
import struct

server_ip = "127.0.0.1"
server_port = 12345

cap = cv2.VideoCapture(0)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(5)
print(f"Server listening on {server_ip}:{server_port}")
client_socket, addr = server_socket.accept()
print(f"Connection from {addr}")
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
while True:
    ret, frame = cap.read()
    data = pickle.dumps(frame)
    message_size = struct.pack("L", len(data))
    client_socket.sendall(message_size + data)

cap.release()
server_socket.close()
cv2.destroyAllWindows()
