#!/bin/bash
# Script to display all methods
curl -sI 0:5000/route_4 | grep "Allow" | cut --character=8-
