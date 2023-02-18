#!/usr/bin/python3
"""
Show Status
Python script that fetches https://intranet.hbtn.io/status
"""


if __name__ == "__main__":
    from urllib import request
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf content: {}".format(html.decode('utf-8')))
