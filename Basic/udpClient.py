import socket

# Using IPv4 and UDP protocol
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_ip = "127.0.0.1"
server_port = 1234

# Function to send messages to the server
def sendMessage():
    while True:
        message = input("Enter the message to send: ")
        client_socket.sendto(message.encode(), (server_ip, server_port))
        print(f"Message sent to {server_ip}:{server_port}")

sendMessage()