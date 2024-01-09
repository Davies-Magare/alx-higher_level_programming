#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let biggest = Number.parseInt(process.argv[2]);
  let i;
  let currentBiggest;
  for (i = 2; i < process.argv.length; i++) {
    currentBiggest = Number.parseInt(process.argv[i]);
    if (currentBiggest > biggest) {
      biggest = currentBiggest;
    }
  }
  const bigIndex = [];
  for (i = 2; i < process.argv.length; i++) {
    if (Number.parseInt(process.argv[i]) === biggest) {
      bigIndex.push(i);
    }
  }
  let secondBiggest = 0;
  for (i = 2; i < process.argv.length; i++) {
    if (Number.parseInt(process.argv[i]) > secondBiggest &&
      !bigIndex.includes(i)) {
      secondBiggest = Number.parseInt(process.argv[i]);
    }
  }
  console.log(secondBiggest);
}
