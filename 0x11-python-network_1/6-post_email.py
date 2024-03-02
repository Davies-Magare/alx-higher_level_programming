#!/usr/bin/python3
"""Take in url, and email, send post
request to passed url with email as parameter
and display body of response.
"""
import requests
import sys
if __name__ == "__main__":
    my_dict = {}
    my_dict['email'] = sys.argv[2]
    try:
        r = requests.post(sys.argv[1], data=my_dict)
        print(r.text)
    except Exception:
        pass
