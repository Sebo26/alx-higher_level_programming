#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

URL = None
Email = None

data = urllib.parse.urlencode({'email': Email}).encode('utf-8')
req = urllib.request.Request(URL, data=data)

with urllib.request.urlopen(req) as response:
    print("Your email is:", response.read().decode('utf-8'))

if __name__ == "__main__":
    main()
