#!/usr/bin/bash
#This script sends a request to the given url and displays
#the body size of the response
curl -sI $1 | grep content-length
