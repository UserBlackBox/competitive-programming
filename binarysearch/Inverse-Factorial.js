// https://binarysearch.com/problems/Inverse-Factorial

class Solution {
    solve(a) {
        let fact = 1;
        let i=1;
        while(fact<=a){
            if(fact===a) return i;
            i++;
            fact*=i;
        }
        return -1;
    }
}
