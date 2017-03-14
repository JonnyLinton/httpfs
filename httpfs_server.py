import socket
import threading
import argparse
from httpfs_helper_functions import handle_get
from httpfs_helper_functions import receive_request


def run_server(port=8086):
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
        data = conn.recv(1024)
        # while True:
        #     print("in loop")
        #     data += conn.recv(256)
        #     print("after recv")
        #     if not data:
        #         break
        print("calling get")
        print(str(data))
        content = receive_request(str(data)).encode("utf-8")
        # split content into smaller pieces?
        print("sending content")
        conn.sendall(content)
    finally:
        conn.close()


# curl localhost:8080/file.txt

if __name__ == '__main__':
   run_server()
