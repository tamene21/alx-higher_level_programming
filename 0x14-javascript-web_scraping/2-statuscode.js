#!/usr/bin/node
// Display the status of  GET Request

const request = require('request');
const url = process.argv[2];

request.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
