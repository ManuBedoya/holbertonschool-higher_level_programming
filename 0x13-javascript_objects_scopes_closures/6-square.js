#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.size; i++) {
      let secuence = '';
      for (let j = 0; j < this.size; j++) {
        secuence += c;
      }
      console.log(secuence);
    }
  }
}

module.exports = Square;
