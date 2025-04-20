#!/usr/bin/env python3
# ipc_server.py

import socket
import json
import statistics

HOST = socket.gethostbyname('ipc_server_dns_name')  # Standard loopback interface address (localhost)
PORT = 9898        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    
    with conn:
        print('Connected by', addr)
        data = conn.recv(4096)
        params = json.loads(data.decode())

        mean_val = statistics.mean(params)
        median_val = statistics.median(params)
        stddev_val = statistics.stdev(params)

        stats = {
            'mean': mean_val,
            'median': median_val,
            'stddev': stddev_val
        }

        print("Received parameters:", params)
        print("Computed stats:", stats)

        conn.sendall(json.dumps(stats).encode())
