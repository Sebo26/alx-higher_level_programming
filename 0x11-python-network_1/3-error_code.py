#!/usr/bin/python3
import urllib.request
import urllib.error
import sys
with urllib.request.urlopen(sys.argv[1]) as response:
    print("Error code: ", response.read().decode('utf-8'))
