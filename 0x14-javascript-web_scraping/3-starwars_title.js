#!/usr/bin/node
const https = require('https');

const url = 'swapi-api.hbtn.io';
const path = `/api/films/${process.argv[2]}/`;
const options = {
  hostname: url,
  port: 443,
  path: path,
  method: 'GET'
};

const req = https.request(options, res => {
  let todo = '';
  res.on('data', (chunk) => {
    todo += chunk;
  });

  // called when the complete response is received.
  res.on('end', () => {
    console.log(JSON.parse(todo).title);
  });
});

req.on('error', error => {
  console.error(error);
});

req.end();
