#!/bin/bash
# Script to size body
curl -sI "$1" | grep "Content-Length" | cut --character=17-
