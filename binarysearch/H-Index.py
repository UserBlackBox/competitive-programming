# https://binarysearch.com/problems/H-Index

import bisect
class Solution:
    def solve(self, citations):
        if citations == []:
            return 0
        citations.sort()
        for i in range(citations[-1],0,-1):
            most = bisect.bisect_left(citations,i)
            if len(citations)-most >= i:
                return i
        return 0
