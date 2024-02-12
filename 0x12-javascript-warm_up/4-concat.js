#!/usr/bin/node
let myArray;
if (process.argv[2] && process.argv[3]) {
  myArray = [process.argv[2], process.argv[3]];
} else if (process.argv[2]) {
  myArray = [process.argv[2], 'undefined'];
} else if (process.argv[3]) {
  myArray = ['undefined', process.argv[3]];
} else {
  myArray = ['undefined', 'undefined'];
}
const arrayStr = myArray.join(' is ');
console.log(arrayStr);
