#!/bin/bash
#This script sends a request to the given url and display the body size of the response
curl -sI "$1" | grep -i Content-Length
