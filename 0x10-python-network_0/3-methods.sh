#!/bin/bash
# displays all HTTP methods the server will accept
URL="https://example.com"
content=$(curl -s -L -X "$URL")
echo "$content"
