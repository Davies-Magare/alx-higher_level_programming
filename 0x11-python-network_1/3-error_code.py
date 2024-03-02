#!/usr/bin/python3
"""Take in URL and display the body of the response
"""
import sys
from urllib.request import urlopen
from urllib.error import HTTPError
if __name__ == '__main__':
    try:
        with urlopen(sys.argv[1]) as response:
            body = response.read()
            decoded_body = body.decode("utf-8")
            print(decoded_body)
    except HTTPError as e:
        print("Error code: {}".format(e.code))
