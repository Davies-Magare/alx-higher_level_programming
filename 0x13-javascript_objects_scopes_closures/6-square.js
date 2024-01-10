#!/usr/bin/node

const square = require('./5-square');
module.exports = class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      let row = '';
      let i;
      let j;
      for (i = 0; i < this.height; i++) {
        for (j = 0; j < this.width; j++) {
          row += c;
        }
        console.log(row);
        row = '';
      }
    }
  }
};
