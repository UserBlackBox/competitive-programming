# https://binarysearch.com/problems/Longest-Consecutive-Run-of-1s-in-Binary

class Solution:
    def solve(self, n):
        binary = bin(n)[2:]
        binary = binary.split('0')
        return len(max(binary,key=len))

