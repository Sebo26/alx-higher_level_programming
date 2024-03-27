#!/bin/bash
# sends a POST request and displays the body of the response
curl -s -L -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$URL"
