#!/usr/bin/node
const Sqr = require('./5-square');
class Square extends Sqr {
  constructor (size) {
    super(size, size);
  }

  print () {
    super.print();
  }

  double () {
    super.double();
  }

  rotate () {
    super.rotate();
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let rowStr;
      for (let i = 0; i < this.height; i++) {
        rowStr = '';
        for (let j = 0; j < this.width; j++) {
          rowStr += c;
        }
        console.log(rowStr);
      }
    }
  }
}
module.exports = Square;
