# https://binarysearch.com/problems/Tree-Sum

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        nums = []
        def addNums(root,n):
            if root == None:
                return
            n.append(root.val)
            addNums(root.left,n)
            addNums(root.right,n)
        addNums(root,nums)
        return sum(nums)

