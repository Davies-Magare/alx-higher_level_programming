#!/usr/bin/node
const request = require('request');
const address = process.argv[2];
request(address, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const result = JSON.parse(body);
    const searchCharacters = function (characters) {
      const searchUrl = function (url) {
        let k = 0; let actors = 0;
        while (k < url.length) {
          if (url[k] === '1' && url[k + 1] === '8') {
            actors++;
          }
          k++;
        }
        return actors;
      };
      let wedgeCount = 0;
      for (let i = 0; i < characters.length; i++) {
        wedgeCount += searchUrl(characters[i]);
      }
      return wedgeCount;
    };
    let wedgeTotal = 0;
    for (let i = 0; i < result.results.length; i++) {
      wedgeTotal += searchCharacters(result.results[i].characters);
    }
    console.log(wedgeTotal);
  } else {
    console.log(error);
  }
});
