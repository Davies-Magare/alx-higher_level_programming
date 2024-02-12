#!/usr/bin/node
let sum;
if (isNaN(process.argv[2]) || isNaN(process.argv[3])) {
  sum = NaN;
} else {
  sum = parseInt(process.argv[2]) + parseInt(process.argv[3]);
}
console.log(sum);
