import socket
import threading

Header = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
# print(socket.gethostname())
ADDR = (SERVER, PORT) # bind
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

print("hello rajendra")

def handle_client(conn, addr):
    '''handle's client request and send message to client'''
    print(f"[NEW CONNETION] {addr} connected.")
    connected = True
    while connected:
        msg_legth = conn.recv(Header).decode(FORMAT)
        if msg_legth:
            msg_legth = int(msg_legth)
            msg = conn.recv(msg_legth).decode(FORMAT)
            if msg==DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))
    conn.close()

def start():
    '''will accept the server request start connection'''
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNETIONS] {threading.activeCount() -1}")

print("[STRATING] server is strating ......")
start()