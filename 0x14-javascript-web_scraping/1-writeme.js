#!/usr/bin/node
const request = require('request');

console.log('code: ' + request.get(process.argv[2]));
