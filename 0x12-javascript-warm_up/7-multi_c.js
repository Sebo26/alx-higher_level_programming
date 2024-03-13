#!/usr/bin/node
let i = process.argv[2];
let j;
if (i === undefined) {
  console.log('Missing number of occurrences');
} else if (i <= 0) {
  process.exit();;
} else {
    for (j = 0; j < i; j++) {
      console.log('C is fun');
    }
}
