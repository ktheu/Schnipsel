
a = [1,2,3]
for (let i = 0; i < a.length; i++) {
  console.log(a[i]);
}
 
a.forEach(function(x) {
  console.log(x);
});

a.forEach((x) => console.log(x));

for (let x of a) {
  console.log(x);
}
