// https://dmoj.ca/problem/dmopc14c2p4
// https://dmoj.ca/submission/2946292
// should be run with v8dmoj

let trees = [];
let n = Number(gets());
trees[0] = Number(gets());
for(let i=1;i<n;i++){
    trees[i] = Number(gets()) + trees[i-1];
}
let q = Number(gets());
let temp;
for(let i=0;i<q;i++){
    temp = gets().split(' ');
    temp[0] = Number(temp[0]);
    temp[1] = Number(temp[1]);
    if(temp[0]===0){
        print(trees[temp[1]]);
        continue;
    }
    print(trees[temp[1]] - trees[temp[0]-1]);
}