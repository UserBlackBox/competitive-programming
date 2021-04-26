# https://binarysearch.com/problems/Sum-of-Two-Numbers-in-BSTs

import bisect

class Solution:
    @staticmethod
    def getList(root, lst):
        if root == None:
            return
        Solution.getList(root.left,lst)
        lst.append(root.val)
        Solution.getList(root.right,lst)

    def solve(self, a, b, target):
        if a == None or b == None:
            return False
        listA = []
        Solution.getList(a,listA)
        listB = []
        Solution.getList(b,listB)
        listB = set(listB)
        for i in listA:
            if target-i in listB:
                return True
        return False

