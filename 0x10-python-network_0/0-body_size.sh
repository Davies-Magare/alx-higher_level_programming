#!/bin/bash
#This script sends a request to the given url and display the body size of the response
if [ #$ -eq 1 ]
then
	curl -sI "$1" | grep -i Content-Length
