#!/bin/bash
# displays all HTTP methods the server will accept
curl -s -L -I | grep "Allow"
