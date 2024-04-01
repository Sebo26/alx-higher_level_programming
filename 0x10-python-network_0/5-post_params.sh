#!/bin/bash
# sends a POST request and displays the body of the response
curl -s -L -X POST -d "$2" "$1"
