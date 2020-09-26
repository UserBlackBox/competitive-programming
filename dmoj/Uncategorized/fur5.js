// https://dmoj.ca/problem/fur5
// https://dmoj.ca/submission/3023943
// should be run with v8dmoj

let n = Number(gets());
let a = [];
let b = [];
let c = [];

function move(n, s, t, ax) {
    if(n>0){
        move(n-1,s,ax,t);
        t.push(s.pop());
        if(s==a){
            if(t==b) print("AB");
            else if(t==c) print("AC");
        }else if(s==b){
            if(t==a) print("BA");
            else if(t==c) print("BC");
        }else if(s==c){
            if(t==a) print("CA");
            else if(t==b) print("CB");
        }
        move(n-1,ax,t,s);
    }
}

for(let i=n;i>0;i--){
    a.pop(i);
}
move(n,a,c,b);
