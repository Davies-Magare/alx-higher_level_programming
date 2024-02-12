#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  function findBiggest () {
    let biggest = 2;
    for (let i = 3; i < process.argv.length; i++) {
      if (process.argv[i] > process.argv[biggest]) {
        biggest = i;
      }
    }
    return (biggest);
  }
  const biggestNum = findBiggest();
  let secondBiggest = 2;
  const subZero = process.argv[biggestNum] - process.argv[2];
  for (let i = 3; i <= process.argv.length; i++) {
    if ((process.argv[biggestNum] - process.argv[i]) !== 0 &&
      (process.argv[biggestNum] - process.argv[i]) < subZero) {
      secondBiggest = i;
    }
  }
  console.log(process.argv[secondBiggest]);
}
