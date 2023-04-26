#!/usr/bin/node
// printing all characterst of allstar move

const request = require('request');
const film = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + film;

request(url, function (error, res, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    charaList(characters, 0);
  }
});

function charaList (characters, index) {
  request(characters[index], function (error, res, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        charaList(characters, index + 1);
      }
    }
  });
}
