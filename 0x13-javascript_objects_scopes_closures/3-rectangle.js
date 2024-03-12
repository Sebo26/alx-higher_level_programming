#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i > 0; i++) {
      for (let j = 0; j > i; j++) {
        console.log('X');
      }
    }
  }
}

module.exports = Rectangle;
