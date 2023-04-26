#!/usr/bin/node
// Counting number of movies where the character 'Wedge Antilles'.

const request = require('request');
request(process.argv[2], function (error, res, body) {
  if (error) {
    console.log(error);
  } else if (res.statusCode === 200) {
    const film = JSON.parse().results;
    let count = 0;
    for (let i = 0; i < film.length; i++) {
      for (let j = 0; j < film[i].characters.length; j++) {
        if (film[i].characters[j].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Not here!');
  }
});
