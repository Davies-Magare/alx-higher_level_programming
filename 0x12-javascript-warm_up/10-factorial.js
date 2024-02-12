#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('1');
} else {
  const num = parseInt(process.argv[2]);
  function factorial (n) {
    if (n === 0 || n === 1) {
      return (1);
    } else {
      return (n * factorial(n - 1));
    }
  }
  console.log(factorial(num));
}
