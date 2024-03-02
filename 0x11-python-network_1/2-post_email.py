#!/usr/bin/python3
"""Take in url, and email, send post
request to passed url with email as parameter
and display body of response.
"""
from urllib import request
from urllib.parse import urlencode
import sys
if __name__ == "__main__":
    dict = {}
    dict['email'] = sys.argv[2]
    url_encoded_data = urlencode(dict)
    send_data = url_encoded_data.encode("utf-8")
    with request.urlopen(sys.argv[1], data=send_data) as response:
        body = response.read()
    decoded_body = body.decode("utf-8")
    print(decoded_body)
