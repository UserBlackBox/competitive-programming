// https://binarysearch.com/problems/FizzBuzz

class Solution {
    solve(n) {
        let lst = [];
        for(let i=1;i<=n;i++){
            let out = ""
            out += (i%3===0?"Fizz":"");
            out += (i%5===0?"Buzz":"");
            out = (out.length===0?i.toString():out);
            lst.push(out);
        }
        return lst;
    }
}
