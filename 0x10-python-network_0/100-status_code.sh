#!/bin/bash
# Script to display the status code
curl -sI -w '%{response_code}' "$1" -o /dev/null
