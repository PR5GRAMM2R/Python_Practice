import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))

    except:
        print(f"Cannot connect to server")
    
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Recieved {data!r}")
