# https://binarysearch.com/problems/Sibling-Tree-Value

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, k):
        if root.left == None and root.right == None:
            return None
        if root.left.val == k:
            return root.right.val
        if root.right.val == k:
            return root.left.val
        left = self.solve(root.left,k)
        right = self.solve(root.right,k)
        if left != None:
            return left
        if right != None:
            return right

