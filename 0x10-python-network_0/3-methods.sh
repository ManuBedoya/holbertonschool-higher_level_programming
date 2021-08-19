#!/bin/bash
# Script to display all methods
curl -sI "$1" | grep "Allow" | cut --character=8-
