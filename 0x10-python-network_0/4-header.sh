#!/bin/bash
#send curl request with header variable
curl -i -s  -H 'X-School-User-Id: 98' $1 | tail -1
