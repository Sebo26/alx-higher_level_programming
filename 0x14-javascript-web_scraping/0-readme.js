#!/usr/bin/node

const fs = require('fs');
const path = process.argv[2];

if (!path) {
  console.error('Please provide a file path as the first argument.');
  process.exit(1);
}

fs.readFile(path, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
  }
  else {
    console.log(data);
  }
});

