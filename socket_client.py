import socket
import time

socket_path = "timer.sock"

with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
    client.connect(socket_path)
    iter = 0
    while True:
        time.sleep(1.0)
        iter += 1
        client.sendall(iter.to_bytes(4, "big"))
        data = client.recv(1024)
        print(data)
