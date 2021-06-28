# https://binarysearch.com/problems/Sum-of-First-N-Odd-Integers

class Solution:
    def solve(self, n):
        return sum([n for n in range(1,n*2,2)])

