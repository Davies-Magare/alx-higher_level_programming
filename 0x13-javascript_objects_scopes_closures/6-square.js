#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row = '';
    let i;
    let j;

    for (i = 0; i < this.height; i++) {
      for (j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
      row = '';
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = class Square extends Rectangle {
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
