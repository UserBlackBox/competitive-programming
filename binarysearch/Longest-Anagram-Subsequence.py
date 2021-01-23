# https://binarysearch.com/problems/Longest-Anagram-Subsequence

class Solution:
    def solve(self, a, b):
        letters = set(list(a)).intersection(set(list(b)))
        length = 0
        for i in letters:
            length += min(a.count(i),b.count(i))
        return length

