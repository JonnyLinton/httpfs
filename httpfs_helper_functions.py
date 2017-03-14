import socket
import re
from file_handling import get_file
from email.utils import formatdate
from datetime import datetime
from time import mktime
from HTTPException import *

def receive_request(data):
    # louis
    request_type = request_type_parsing(data)
    header_dictionary = header_parsing(data)
    pathname = pathname_parsing(data)
    print("Inside receive_request, pathname:" +pathname)
    body = body_parsing(data)
    if request_type == "GET":
        return handle_get(header_dictionary, pathname)
    elif request_type == "POST":
        return handle_post(header_dictionary, body, pathname)
    else:
        raise HTTPException(400)

def handle_get(header_dictionary, path):
    # returns GET response headers and body
    body = get_file(path)

    response = '''HTTP/1.1 200 OK
    Date: ''' +getDate() +'''
    Content-Type: text\r\n\r\n''' +body

    return response

def handle_post(request_headers_and_data):
    # Louis-Olivier
    # returns POST response headers and body
    return True

def header_parsing(header):
    dict = {}
    lines =  re.split("\n+", header)
    requests_list = [re.split(": ", entry, 2) for entry in lines]
    for elements in requests_list:
        if len(elements) > 1:
            dict[elements[0]] = elements[1]
    return dict

def request_type_parsing(header):
    # print("Inside request_type_parsing, header: " + header)
    return re.search(r"^[^ /]*", header).group(0)

def pathname_parsing(header):
    # print("Inside pathname_parsing, header: " + header)
    return re.search(r"\s(.*?)\s", header).group(0).replace(" ", "")

def body_parsing(request):
    # print("Inside body_parsing, request: " + request)
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
