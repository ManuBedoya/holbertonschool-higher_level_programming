#!/usr/bin/node
const request = require('request');

const users = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

request(process.argv[2], function (error, response, body) {
  if (error) { console.log(error); }
  const array = JSON.parse(body);
  for (let i = 0; i < array.length; i++) {
    if (array[i].completed) { users[array[i].userId - 1]++; }
  }
  let res = '{ ';
  for (let i = 0; i < users.length; i++) {
    if (i === users.length - 1) {
      res += `'${i + 1}': ${users[i]} }`;
    } else {
      res += `'${i + 1}': ${users[i]}\n  `;
    }
  }
  console.log(res);
});
