#!/usr/bin/python3
"""
Take a url and display the body of the response
"""
import requests
import sys
try:
    r = requests.get(sys.argv[1])
    if r.status_code < 400:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
except Exception:
    pass
