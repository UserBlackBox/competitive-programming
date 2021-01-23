# https://binarysearch.com/problems/Search-in-a-Binary-Search-Tree

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import bisect
class Solution:
    def solve(self, root, val):
        if root == None:
            return False
        elif root.val == val:
            return True
        elif root.val > val:
            return self.solve(root.left,val)
        elif root.val < val:
            return self.solve(root.right,val)
        return None
