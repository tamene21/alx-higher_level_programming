#!/usr/bin/node
// accessing the contents of the web page

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (error, res, body) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(process.argv[3], body, 'utf8', function (error) {
    if (error) {
      console.log(error);
    }
  });
});
