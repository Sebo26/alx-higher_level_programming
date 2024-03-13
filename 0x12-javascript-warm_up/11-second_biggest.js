#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let args = process.argv.slice(2).map(Number);

  if (args.length <= 1) {
    console.log(0);
  } else {
    args = args.sort((a, b) => b - a);
    console.log(args[1]);
  }
}
