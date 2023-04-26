#!/usr/bin/node
// writing a string

const fs = require('fs');
const argv = process.argv;
const filePath = argv[2];
const string = argv[3];

fs.writeFile(filePath, string, 'utf8', function (error) {
  if (error) {
    console.log(error);
  }
});
