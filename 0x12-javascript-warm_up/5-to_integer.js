#!/usr/bin/node
const inputString = process.argv[2];
const num = Number.parseInt(inputString);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(num);
}
