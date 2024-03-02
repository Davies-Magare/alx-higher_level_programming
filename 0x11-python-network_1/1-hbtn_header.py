#!/usr/bin/python3
"""Take in url, send a request and display the
value of x-Request-Id variable in the header of
the response.
"""
from urllib import request
import sys
with request.urlopen(sys.argv[1]) as response:
    print(response.getheader('X-Request-Id'))
