# https://binarysearch.com/problems/Pascal's-Triangle
# https://binarysearch.com/problems/Pascal's-Triangle/submissions/1040848

from math import comb  # import choose notation function

class Solution:
    def solve(self, n):
        row = []
        for i in range(0, n + 1):  # loop through all values in row
            row.append(comb(n, i))  # calculate row column value
        return row

