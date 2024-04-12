import os
import socket
from datetime import datetime

socket_path = "timer.sock"

try:
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as server:
        server.bind(socket_path)
        server.listen(1)
        conn, client = server.accept()
        print(f"Connection from: {conn}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(int.from_bytes(data, "big"))
            timestamp = datetime.now()
            conn.sendall(timestamp.__str__().encode())
finally:
    os.unlink(socket_path)
