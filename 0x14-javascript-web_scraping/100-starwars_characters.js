#!/usr/bin/node
// printing all characterst of allstar move

const request = require('request');
const film = process.argv[2];
const url = 'https://swapi.co/api/films/' + film;
request(url, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const movie = JSON.parse(body);
  for (const character of movie.characters) {
    request(character, function (error, res, body) {
      if (error) {
        console.log(error);
      }
      const chr = JSON.parse(body);
      console.log(chr.name);
    });
  }
});
