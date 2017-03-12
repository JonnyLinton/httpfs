import socket
import re
def handle_get(request_headers):
    # Jonny
    # returns GET response headers and body
    return True

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
