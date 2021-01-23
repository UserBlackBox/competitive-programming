# https://binarysearch.com/problems/Making-Change

class Solution:
    def solve(self, n):
        coins = 0
        coins += n//25
        n -= 25*(n//25)
        coins += n//10
        n -= 10*(n//10)
        coins += n//5
        n -= 5*(n//5)
        coins += n
        return coins
