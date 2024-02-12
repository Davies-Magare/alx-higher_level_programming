#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  function findBiggest () {
    let biggest = 2;
    for (let i = 3; i < process.argv.length; i++) {
      if (parseInt(process.argv[i]) > parseInt(process.argv[biggest])) {
        biggest = i;
      }
    }
    return (biggest);
  }
  const biggestNum = findBiggest();
  let secondBiggest = 2;
  const subZero = parseInt(process.argv[biggestNum]) - parseInt(process.argv[2]);
  for (let i = 3; i < process.argv.length; i++) {
    if ((parseInt(process.argv[biggestNum]) - parseInt(process.argv[i])) !== 0 &&
      (parseInt(process.argv[biggestNum]) - parseInt(process.argv[i])) < subZero) {
      secondBiggest = i;
    }
  }
  console.log(parseInt(process.argv[secondBiggest]));
}
