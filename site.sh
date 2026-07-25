#!/bin/bash



SITE="google.com"

ping -c 2 $SITE > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "Site is up"
else
    echo "Site is down"
fi