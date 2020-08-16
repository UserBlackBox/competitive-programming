// https://dmoj.ca/problem/ccc00j2
// https://dmoj.ca/submission/2426231
// should be run with v8dmoj

let m = Number(gets());
let n = Number(gets());
let count = 0
 
function flip(x){
   let y = String(x).split("").reverse()
   if(y.includes('2') || y.includes('3') || y.includes('4') || y.includes('5') || y.includes('7')) return false;
   for(let i=0;i<y.length;i++){
       if(y[i] === '9') y[i] = '6';
       else if(y[i] === '6') y[i] = '9';
   }
   return Number(y.join('')) == x;
}

for(let i=m;i<=n;i++){
    if(flip(i)) count+=1;
}
print(count);