#!/usr/bin/node
module.exports.esrever = function (list) {
  const list_rev = [];
  const len = list.length;
  for (let i = 0; i < len; i++) {
    list_rev.push(list.pop());
  }
  return list_rev;
};
