import socket


HEADER = 64
PORT = 5050
SERVER = '172.21.240.1'
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    '''send's message to client'''
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


# multiple clients connects to the server 
send("hello world!")
input()
send("hy server!")
input()
send("hello dev!")
input()
send("disconnected!")
