#!/usr/bin/python3
import urllib.request
import sys
URL = None
with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers.get('X-Request-Id'))
