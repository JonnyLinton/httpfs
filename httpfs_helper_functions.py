import socket
import re
from file_handling import get_file
from file_handling import post_file
from email.utils import formatdate
from datetime import datetime
from time import mktime
from HTTPException import *
from logger_init import logger

def receive_request(request_data, verbose, server_working_directory):
    logger.info("Request Received")
    request_type = request_type_parsing(request_data)
    header_dictionary = header_parsing(request_data)
    path_from_request = pathname_parsing(request_data)
    print("This is the path from request: ", path_from_request)
    print("Inside receive_request, path_from_request:" +path_from_request)
    body = body_parsing(request_data)
    if request_type == "GET":
        logger.info("Request is of type GET %s", path_from_request)
        return handle_get(header_dictionary, path_from_request, verbose, server_working_directory)
    elif request_type == "POST":
        logger.info("Request is of type POST %s", path_from_request)
        return handle_post(header_dictionary, body, path_from_request, verbose, server_working_directory)
    else:
        raise HTTPException(400)

def handle_get(header_dictionary, path_from_request, verbose, server_working_directory):
    # returns GET response headers and body
    body = get_file(path_from_request, verbose, server_working_directory)

    response = "HTTP/1.1 200 OK\r\nDate: " +getDate() +"\r\n\r\n" +body

    return response

def handle_post(header_dictionary, body, path_from_request, verbose, server_working_directory):
    # returns POST response headers and body
    body = post_file(path_from_request, body, verbose, server_working_directory, overwrite=True)

    response = "HTTP/1.1 200 OK\r\nDate: " + getDate() +"\r\n\r\n" + body

    return response

def header_parsing(header):
    dict = {}
    lines =  re.split("\n+", header)
    requests_list = [re.split(": ", entry, 2) for entry in lines]
    for elements in requests_list:
        if len(elements) > 1:
            dict[elements[0]] = elements[1]
    return dict

def request_type_parsing(header):
    return re.search(r"^[^ /]*", header).group(0)

def pathname_parsing(header):
    return re.search(r"\s(.*?)\s", header).group(0).replace(" ", "")

def body_parsing(request):
    data_content = request.split("\r\n\r\n")
    if len(data_content) > 1:
        return data_content[1]
    else:
        return ""

def getDate():
    now = datetime.now()
    stamp = mktime(now.timetuple())
    return formatdate(
        timeval     = stamp,
        localtime   = False,
        usegmt      = True
    )
