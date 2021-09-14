#!/usr/bin/node
// const protocol = require('https')
const https = require('https');

let countSlash = 0;
let before = '';
let after = '';
for (let i = 0; i < process.argv[2].length; i++) {
  if (process.argv[2][i] === '/') {
    countSlash++;
  }
  if (countSlash >= 3) {
    after += process.argv[2][i];
  } else if (countSlash === 2 && process.argv[2][i] !== '/') {
    before += process.argv[2][i];
  }
}
const options = {
  hostname: before,
  port: 443,
  path: after,
  method: 'GET'
};

const req = https.request(options, res => {
  console.log(`code: ${res.statusCode}`);
});

req.on('error', error => {
  console.error(error);
});

req.end();
