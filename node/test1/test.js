const fs = require('fs');
let x = fs.readFileSync('input.txt', 'utf-8');
let res = x.split('\r\n');
console.log(res)