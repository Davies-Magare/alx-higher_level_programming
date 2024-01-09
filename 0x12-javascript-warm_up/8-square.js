#!/usr/bin/node
const num = Number.parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  let i;
  let j;
  let row = '';
  for (i = 0; i < num; i++) {
    for (j = 0; j < num; j++) {
      row += 'X';
    }
    console.log(row);
    row = '';
  }
}
