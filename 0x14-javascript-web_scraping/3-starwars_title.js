#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
request(`https://swapi-api.alx-tools.com/api/films/${id}`, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const result = JSON.parse(body);
    console.log(result.title);
  } else {
    console.log(error);
  }
});
