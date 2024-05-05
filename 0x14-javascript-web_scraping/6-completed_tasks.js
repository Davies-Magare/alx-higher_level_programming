#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const result = JSON.parse(body);
    const completeDict = {};
    for (let i = 0, counter = 0; i < result.length; i++) {
      if (result[i].completed === true) {
        completeDict[counter] = result[i].id;
        counter++;
      }
    }
    console.log(completeDict);
  } else {
    console.log(error);
  }
});
