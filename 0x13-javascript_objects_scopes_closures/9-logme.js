#!/usr/bin/node
let counter = -1;
module.exports.logMe = function (item) {
  counter++;
  console.log(`${counter}: ${item}`);
};
