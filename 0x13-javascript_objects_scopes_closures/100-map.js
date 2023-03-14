#!/usr/bin/node
const list = require('./100-data').list;

const lists = list.map(function (x, i) {
  return x * i;
});

console.log(list);
console.log(lists);
