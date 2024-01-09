#!/usr/bin/node
function factorial (num) {
  if (num === 1) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
};
const input = Number.parseInt(process.argv[2]);
if (!isNaN(input)) {
  console.log(factorial (input))
}
