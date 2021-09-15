#!/usr/bin/node
const request = require('request');


const num = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + number;

request.get(url, (err, res, body) => {
  if (err) return (console.log(err));
  const movies = JSON.parse(body);

  movies.characters.forEach(charUrl => request.get(charUrl, (err, res, body) => {
    if (err) return (console.log(err));
    console.log(JSON.parse(body).name);
  }));
});
