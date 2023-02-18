#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)"""


if __name__ == "__main__":
    from urllib import parse, request
    from sys import argv
    email = parse.urlencode({"email": argv[2]}).encode('utf-8')
    url = request.Request(argv[1], email)
    with request.urlopen(url) as response:
        req = response.read().decode('utf-8')
        print("{}".format(req))
