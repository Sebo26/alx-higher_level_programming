#!/bin/bash
# displays the size of the body of the response
URL="https://example.com"
content=$(curl -s -L "$URL")
content_length=$(echo -n "$content" | wc -c)
