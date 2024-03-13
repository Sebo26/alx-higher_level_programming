#!/usr/bin/node
function add (a, b) {
  if (!isNaN(parseInt(a)) && !isNaN(parseInt(b))) {
    const c = parseInt(a) + parseInt(b);
    console.log(c);
  } else {
    console.log('NaN');
  }
}
