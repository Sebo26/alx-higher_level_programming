#!/bin/bash
# displays the size of the body of the response
curl -s -L "$1" | wc -c
