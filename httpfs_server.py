import socket
import threading
import argparse
from httpfs_helper_functions import handle_get
from httpfs_helper_functions import receive_request
from HTTPException import *
from logger_init import logger

def run_server(verbose, server_working_directory, port=8081):
    # Disable the logger if verbose is False
    logger.disabled = not verbose
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
        response = "".encode("utf-8")
        try:
            response = receive_request(data.decode("utf-8"), verbose, str(server_working_directory))
            response = response.encode("utf-8")
        except HTTPException as e:
            # catch any HTTPExceptions and instead transform it into the appropriate response code
            http_code = e.args[0]
            http_code_name = http_name_from_code(http_code)
            response = "HTTP/1.1 " +str(http_code) +" " +http_code_name +"\r\n\r\n"
            response = response.encode("utf-8")
        finally:
            print("\nSending response: \n" +response.decode("utf-8"))
            conn.sendall(response)
    finally:
        conn.close()

def http_name_from_code(http_code):
    if(http_code == 400):
        return "Bad Request"
    elif(http_code == 403):
        return "Forbidden"
    elif(http_code == 404):
        return "Not Found"
    else:
        raise Exception("Louis and Jonny have not finished their code correctly")
