# https://binarysearch.com/problems/No-New-Friends

class Solution:
    def solve(self, n, friends):
        hasFriend = []
        for i in range(n):
            hasFriend.append(False)
        for i in friends:
            hasFriend[i[0]] = True
            hasFriend[i[1]] = True
        return all(hasFriend)
