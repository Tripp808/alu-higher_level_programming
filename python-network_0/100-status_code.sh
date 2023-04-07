#!/bin/bash

# Send a request to the URL passed as an argument and display only the status code of the response.

# Check if an argument was passed
if [ $# -eq 0 ]; then
  echo "Error: No URL provided."
  exit 1
fi

# Send a request to the URL and store the response status code in a variable
STATUS=$(curl -s -o /dev
