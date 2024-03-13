#!/usr/bin/node
function factorial (a) {
  let fact = 1;

  if (isNaN(a)) {
    fact = 1;
  } else {
    for (let i = 1; i <= a; i++) {
      fact *= i;
    }
  }

  return fact;
}

console.log(factorial(Number(process.argv[2])));
