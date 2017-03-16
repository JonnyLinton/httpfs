import socket
import os
import threading
import argparse
from httpfs_helper_functions import handle_get
from httpfs_helper_functions import receive_request
from HTTPException import *
from logger_init import logger

def run_server(verbose, server_working_directory, port=8080):
    # Disable the logger if verbose is False
    logger.disabled = not verbose
    logger.warning("Server initialized at port %s", port)
    port = int(port)
    host = ''
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        listener.bind((host, port))
        listener.listen(5)
        print('HTTPfs is listening at', port)
        while True:
            threading.Thread(target=end_server).start()
            conn, addr = listener.accept()
            threading.Thread(target=handle_client, args=(conn, addr, verbose, server_working_directory)).start()

    finally:
        listener.close()

def handle_client(conn, addr, verbose, server_working_directory):
    logger.info('New connection: %s', str(addr))
    try:
        data = conn.recv(1024)
        print("Receiving request: \n" +data.decode("utf-8"))
        response = "".encode("utf-8")
        try:
            response = receive_request(data.decode("utf-8"), verbose, str(server_working_directory))
            response = response.encode("utf-8")
        except HTTPException as e:
            # catch any HTTPExceptions and instead transform it into the appropriate response code
            http_code = e.args[0]
            http_code_name = http_name_from_code(http_code)
            response = "HTTP/1.1 " +str(http_code) +" " +http_code_name +"\r\n\r\nError " +str(http_code) +" (" +http_code_name +") \n"
            response = response.encode("utf-8")
        finally:
            print("\nSending response: \n" +response.decode("utf-8"))
            conn.sendall(response)
    finally:
        logger.info("Connection with client %s closed.", str(addr))
        conn.close()

def end_server():
    user_input = input()
    if user_input == "exit":
        os._exit(1)

def http_name_from_code(http_code):
    if(http_code == 400):
        logger.error("Bad Request %i", http_code)
        return "Bad Request"
    elif(http_code == 403):
        logger.error("Forbidden %i", http_code)
        return "Forbidden"
    elif(http_code == 404):
        logger.error("Not Found %i", http_code)
        return "Not Found"
    else:
        logger.error("Exceptional Exception: %i", http_code)
        return "Something went wrong. Please submit your request again."
