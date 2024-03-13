#!/usr/bin/node
const c;
function add(a, b) {
  if (!isNaN(parseInt(a)) && !isNaN(parseInt(b))) {
    c = parseInt(a) + parseInt(b);
    console.log(c);
  } else {
  console.log('NaN')
  }
}
