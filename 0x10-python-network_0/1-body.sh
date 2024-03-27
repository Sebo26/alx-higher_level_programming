#!/bin/bash
# displays the body of the response
URL="https://example.com"
content=$(curl -s -L "$URL")
if [ "$http_status" -eq 200 ]; then
	body=$(echo "$content" | sed -n '1,/^$/p' | sed '$d')
    echo "$body"
fi
