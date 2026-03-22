#!/usr/bin/node
const num = parseInt(process.argv[2]);
let i = 0;

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  while (i < num) {
    console.log('C is fun');
    i++;
  }
}
