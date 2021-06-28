// https://binarysearch.com/problems/Furthest-From-Origin

class Solution {
    solve(s) {
        let distance = 0;
        let unknown = 0;
        for(let i=0;i<s.length;i++){
            if(s[i]=='L') distance -=1;
            if(s[i]=='R') distance += 1;
            if(s[i]=='?') unknown += 1;
        }
        return Math.abs(distance)+unknown;
    }
}
