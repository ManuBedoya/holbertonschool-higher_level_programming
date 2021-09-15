#!/usr/bin/node
const request = require('request');

const users = {};

request(process.argv[2], function (error, response, body) {
  const array = JSON.parse(body);
  const numberUsers = array[array.length - 1].userId;
  for (let i = 1; i <= numberUsers; i++) {
    users[i] = 0;
  }
  if (error) { console.log(error); }
  for (let i = 0; i < array.length; i++) {
    if (array[i].completed) {
      users[array[i].userId]++;
    }
  }
  console.log(users);
});
