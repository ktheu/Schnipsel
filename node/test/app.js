const fs = require('fs');
// let x = fs.readFileSync('C:\\Users\\khthe\\Documents\\InformatikKurse\\Schnipsel\\node\\test\\input.txt', 'utf-8');
 
let x = fs.readFileSync('./input.txt', 'utf-8');
let res = x.split('\r\n');
console.log(res)

