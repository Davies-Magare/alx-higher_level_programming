#!/usr/bin/node
const num = Number.parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  let i;
  for (i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
