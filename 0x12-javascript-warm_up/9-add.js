#!/usr/bin/node
function add (a, b) {
  const c = parseInt(a) + parseInt(b);
  console.log(c);
}

add(Number(process.argv[2]), Number(process.argv[3]));
