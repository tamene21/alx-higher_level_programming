#!/usr/bin/node
// print a matched starware movie title and episode number

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/:id';

request(url + process.argv[2], function (error, res, body) {
  if (error) {
    console.log(error);
  } else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
