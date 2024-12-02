import socket
import sys

def create_socket():
    try:
        global host
        global port
        global s
        host = "0.0.0.0"  # Listen on all interfaces
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print(f"Socket creation error: {msg}")

def bind_socket():
    try:
        print(f"Binding to port {port}")
        s.bind((host, port))
        s.listen(5)
        print("Listening for connections...")
    except socket.error as msg:
        print(f"Binding error: {msg}\nRetrying...")
        bind_socket()

def socket_accept():
    conn, address = s.accept()
    print(f"Connection established with {address[0]}:{address[1]}")
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input("Command> ")
        if cmd.lower() == "quit":
            conn.close()
            s.close()
            sys.exit()
        elif cmd:
            conn.send(cmd.encode())
            client_response = conn.recv(20480).decode("utf-8", errors="replace")
            print(client_response)

if __name__ == "__main__":
    create_socket()
    bind_socket()
    socket_accept()
