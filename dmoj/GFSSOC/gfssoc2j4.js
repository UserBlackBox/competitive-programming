// https://dmoj.ca/problem/gfssoc2j4
// https://dmoj.ca/submission/2960851
// run with v8dmoj

var temp;
temp = gets().split(' ');
var n = Number(temp[0]);
var q = Number(temp[1]);
temp = gets().split(' ');
var psum = [0];
for(let i=0;i<n;i++){
    psum.push(psum[i]+Number(temp[i]));
}
var total = psum[psum.length-1];
for(let x=0;x<q;x++){
    temp = gets().split(' ');
    temp[0] = Number(temp[0]);
    temp[1] = Number(temp[1]);
    print(total-(psum[temp[1]]-psum[temp[0]-1]));
}
