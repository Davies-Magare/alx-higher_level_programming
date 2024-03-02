#!/usr/bin/python3
"""A python script that fetches
https://alx-intranet.hbtn.io/status
"""
from urllib.request import urlopen
url = "https://alx-intranet.hbtn.io/status"
with urlopen(url) as response:
    body = response.read()
print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
content = body.decode('utf-8')
utf8 = "\t- utf8 content: {}".format(content)
print(utf8)
