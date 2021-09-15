#!/usr/bin/node
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/', function (error, response, body) {
  if (error) { console.error('error:', error); }
  const array = JSON.parse(body).results;
  let count = 0;
  for (let i = 0; i < array.length; i++) {
    for (let j = 0; j < array[i].characters.length; j++) {
      if (array[i].characters[j].split('/')[5] === 18 + '') {
        count++;
      }
    }
  }
  console.log(count);
});
