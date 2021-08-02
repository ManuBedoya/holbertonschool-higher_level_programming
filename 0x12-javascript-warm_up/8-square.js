#!/usr/bin/node

const number = parseInt(process.argv[2]);

if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    let secuence = '';
    for (let j = 0; j < number; j++) {
      secuence += 'X';
    }
    console.log(secuence);
  }
}
