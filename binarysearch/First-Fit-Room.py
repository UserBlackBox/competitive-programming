# https://binarysearch.com/problems/First-Fit-Room

class Solution:
    def solve(self, rooms, target):
        for i in rooms:
            if i >= target:
                return i
        return -1

