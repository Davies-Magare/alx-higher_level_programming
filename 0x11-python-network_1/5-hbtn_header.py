#!/usr/bin/python3
"""Take in url, send a request and display the
value of x-Request-Id variable in the header of
the response.
"""
import requests
import sys
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
