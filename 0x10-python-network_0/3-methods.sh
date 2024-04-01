#!/bin/bash
# displays all HTTP methods the server will accept
curl -s -L -I "$1" | grep -i
