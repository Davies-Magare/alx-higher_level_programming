#!/bin/bash
#Take URL, send request and display size of response body
curl -sI $1 | grep "Content-Length" | cut -d ' ' -f2
