#!/usr/bin/python3
import urllib.request
import sys
URL = None
with urllib.request.urlopen(URL) as response:
    print(response.headers.get('X-Request-Id'))
