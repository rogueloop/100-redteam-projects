import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "127.0.0.1"
port = 1234
s.bind((ip, port))
def receiveMessages():
    print("Server started at and waiting for messages at", ip ,":",port)
    while True:
        data, addr = s.recvfrom(1024)
        message = data.decode()
        print(f'Received message from {addr}:{message}')
receiveMessages()

