#!/usr/bin/node
const i = process.argv[2];
let j;
let k;
if (process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (j = 0; j < i; j++) {
    let row = '';
    for (k = 0; k < i; k++) {
      row += 'X';
    }
    console.log(row);
  }
}
