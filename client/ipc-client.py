#!/usr/bin/env python3
# ipc_client.py

import socket
import json
import random

HOST = socket.gethostbyname('ipc_server_dns_name')  # The server's hostname or IP address
PORT = 9898        # The port used by the server

params = [random.uniform(0, 100) for _ in range(60)]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(json.dumps(params).encode())
    data = s.recv(1024)

stats = json.loads(data.decode())
print("Sent parameters:", params)
print("Received stats:", stats)
