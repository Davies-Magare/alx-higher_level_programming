#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const result = JSON.parse(body);
    const todictIds = function (dict) {
      const idArray = [];
      for (let i = 0; i < result.length; i++) {
        if ((result[i].id in idArray === false) && result[i].completed === true) {
          idArray.push(result[i].userId);
          i++;
        }
      }
      idArray.sort();
      const idDict = {};
      for (let i = 0; i < idArray.length; i++) {
        idDict[idArray[i]] = 0;
      }
      return idDict;
    };
    const idDict = todictIds(body);
    for (let i = 0; i < result.length; i++) {
      if (result[i].completed === true) {
        idDict[result[i].userId] += 1;
      }
    }
    console.log(idDict);
  } else {
    console.log(error);
  }
});
