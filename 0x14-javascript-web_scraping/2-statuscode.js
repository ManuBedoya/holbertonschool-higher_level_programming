#!/usr/bin/node
// const protocol = require('https')
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) { console.error('error:', error); }
  console.log('code:', response.statusCode);
});
