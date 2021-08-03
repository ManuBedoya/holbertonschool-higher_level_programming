#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      this.letter = 'X';
    } else {
      this.letter = c;
    }
    this.print();
  }
}

module.exports = Square;
