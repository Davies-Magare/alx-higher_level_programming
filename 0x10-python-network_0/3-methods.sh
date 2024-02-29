#!/bin/bash
#display all http methods
curl -i -s  $1 | grep "Allow:"| cut -d ' ' -f2-
