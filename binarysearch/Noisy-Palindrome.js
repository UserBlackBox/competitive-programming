// https://binarysearch.com/problems/Noisy-Palindrome

class Solution {
    solve(s) {
        s = s.split("").filter(c => c >= 'a' && c <= 'z').join("");
        return s === s.split("").reverse().join("");
    }
}
