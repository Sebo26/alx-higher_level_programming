#!/usr/bin/node
exports.logMe = function (item) {
  let count = 0;
  for (let i = 0; i < item.length; i++) {
    console.log(count + ': ' + item[i]);
    count++;
  }
};
