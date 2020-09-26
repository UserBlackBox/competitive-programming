// https://dmoj.ca/problem/acmtryouts0b
// https://dmoj.ca/submission/3015363
// should be run with v8dmoj

let t = Number(gets());
for(let i=0;i<t;i++){
    let n = Number(gets());
    let pile = "";
    let first = gets();
    let second = gets();
    for(let j=0;j<n;j++){
        pile += first.charAt(j);
        pile += second.charAt(j);
    }
    pile = pile.split("").reverse().join("");
    print(pile);
}
