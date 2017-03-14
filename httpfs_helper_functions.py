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

sampleRequestGET = '''GET / HTTP/1.1
Host: louisolivier.com
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding: gzip, deflate, sdch
Accept-Language: en,en-US;q=0.8,fr-CA;q=0.6,fr;q=0.4
'''

sampleRequestPOST = '''POST /path/script.cgi HTTP/1.0
From: frog@jmarshall.com
User-Agent: HTTPTool/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 32

home=Cosby&favorite+flavor=flies'''

def receive_request(data):
    # louis
    request_type = request_type_parsing(data)
    header_dictionary = header_parsing(data)
    pathname = pathname_parsing(data)
    body = body_parsing(data)
    if request_type == "GET":
        handle_get(header_dictionary, pathname)
    elif request_type == "POST":
        handle_post(header_dictionary, body, pathname)
    else:
        raise HTTPException(400)



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

def request_type_parsing(header):
    return re.search(r"^[^ /]*", header).group(0)

def pathname_parsing(header):
    return re.search(r"\s(.*?)\s", header).group(0)

def body_parsing(request):
    data_content = request.split("\r\n\r\n")
    if len(data_content) > 1:
        return data.split("\r\n\r\n")[1]
    else:
        return ""

print(body_parsing(sampleRequestPOST))
