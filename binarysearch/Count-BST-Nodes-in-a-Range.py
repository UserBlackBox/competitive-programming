# https://binarysearch.com/problems/Count-BST-Nodes-in-a-Range

import bisect

class Solution:
    @staticmethod
    def getList(root, lst):
        if root == None: return
        else:
            Solution.getList(root.left, lst)
            lst.append(root.val)
            Solution.getList(root.right, lst)

    def solve(self, root, lo, hi):
        lst = []
        Solution.getList(root, lst)
        left = bisect.bisect_left(lst, lo)
        right = bisect.bisect_right(lst, hi)
        return len(lst[left:right])

