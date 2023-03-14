#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let S = '';
      for (let j = 0; j < this.width; j++) {
        S += 'X';
      }
      console.log(S);
    }
  }

  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  double () {
    this.widht *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
