#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
const entries = Object.entries(dict);
entries.forEach(([key, value]) => {
  if (value in newDict) {
    newDict[value].push(key);
  } else {
    newDict[value] = [key];
  }
});
console.log(newDict);
