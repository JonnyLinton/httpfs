import socket
import threading
import argparse


def run_server(verbose, directory, port=8080):
    # port = int(port)
    host = ''
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        listener.bind((host, port))
        listener.listen(5)
        print('Echo server is listening at', port)
        while True:
            conn, addr = listener.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()
    finally:
        listener.close()

def handle_client(conn, addr):
    print ('New client from', addr)
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
    finally:
        conn.close()
