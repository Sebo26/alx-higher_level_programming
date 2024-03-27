#!/bin/bash
# sends delete request and displays response
URL="https://example.com"
content=$(curl -s -L -X DELETE "$URL")
echo "$content" > fetched_content.txt
rm fetched_content.txt
echo "I'm a DELETE request"
