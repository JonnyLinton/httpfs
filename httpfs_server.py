import socket
import threading
import argparse
from httpfs_helper_functions import handle_get
from httpfs_helper_functions import receive_request


def run_server(verbose, server_working_directory, port=8080):
    port = int(port)
    host = ''
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        listener.bind((host, port))
        listener.listen(5)
        print('http file server is listening at', port)
        while True:
            conn, addr = listener.accept()
            threading.Thread(target=handle_client, args=(conn, addr, verbose, server_working_directory)).start()
    finally:
        listener.close()

def handle_client(conn, addr, verbose, server_working_directory):
    print ('New client from', addr)
    try:
        data = conn.recv(1024)
        # while True:
        #     print("in loop")
        #     data += conn.recv(256)
        #     print("after recv")
        #     if not data:
        #         break
        print("Receiving request: \n" +data.decode("utf-8"))
        response = receive_request(data.decode("utf-8"), verbose, str(server_working_directory))
        response = response.encode("utf-8")
        # split content into smaller pieces?
        print("\nSending response: \n" +response.decode("utf-8"))
        conn.sendall(response)
    finally:
        conn.close()
