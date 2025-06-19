import socket
import threading

def receive_messages(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"Received from {addr}: {data.decode('utf-8')}")

def send_messages(sock, remote_addr):
    while True:
        message = input("Enter your message: ")
        sock.sendto(message.encode('utf-8'), remote_addr)

# Your phone's IPv4 address and port (as displayed in UDP Monitor)
phone_ip = '172.23.24.62'
phone_port = 12345

# Your PC's IPv4 address and port 
pc_ip = '0.0.0.0'
pc_port = 12345

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.bind((pc_ip, pc_port))


remote_address = (phone_ip, phone_port)

receive_thread = threading.Thread(target=receive_messages, args=(udp_socket,))
send_thread = threading.Thread(target=send_messages, args=(udp_socket, remote_address))


receive_thread.start()
send_thread.start()

receive_thread.join()
send_thread.join()
