#!/usr/bin/python3
"""Take in a letter and send a post request to url
with the letter as a parameter
"""
import requests
import sys
if __name__ == "__main__":
    payload = {}
    arg = ""
    if len(sys.argv) >= 2:
        arg = sys.argv[1]
    payload["q"] = arg
    url = "http://0.0.0.0:5000/search_user"
    try:
        r = requests.post(url, data=payload)
        if r.status_code >= 500:
            print("Not a valid Json")
        else:
            try:
                json_str = r.json()
                if not json_str:
                    print("No result")
                else:
                    print("[{}] {}".format(json_str['id'], json_str['name']))
            except Exception:
                print("Not a valid Json")
    except Exception:
        pass
