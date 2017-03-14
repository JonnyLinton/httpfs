import socket
import re
from file_handling import get_file
from email.utils import formatdate
from datetime import datetime
from time import mktime

sampleResponseString = '''HTTP/1.1 200 OK
Date: Sun, 26 Sep 2010 20:09:20 GMT
Server: Apache/2.0.52 (CentOS)
Last-Modified: Tue, 30 Oct 2007 17:00:02
Accept-Ranges: bytes
Content-Length: 2652
Keep-Alive: timeout=10, max=100
Connection: Keep-Alive
Content-Type: text/html

data data data data data'''

def receive_request(data):
    # louis

def getDate():
    now = datetime.now()
    stamp = mktime(now.timetuple())
    return formatdate(
        timeval     = stamp,
        localtime   = False,
        usegmt      = True
    )

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
