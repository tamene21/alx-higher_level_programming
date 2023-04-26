#!/usr/bin/node
// Printing commpleted tasks from the todo list

const request = require('request');

request(process.argv[2], function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const tasks = JSON.parse(body);
  const obj = {};
  for (const todo of tasks) {
    if (todo.completed === true) {
      if (obj[todo.userId] === undefined) {
        obj[todo.userId] = 1;
      } else {
        obj[todo.userId]++;
      }
    }
  }
  console.log(obj);
});
