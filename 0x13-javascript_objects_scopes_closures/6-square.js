#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c == undefined) {
	    c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
	    let secuence = '';
	    for (let j = 0; j < this.height; j++) {
        secuence += c;
	    }
	    console.log(secuence);
    }
  }
}

module.exports = Square;
