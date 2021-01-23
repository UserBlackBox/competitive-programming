# https://binarysearch.com/problems/Most-Frequent-Subtree-Sum

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        sums = []
        def collect(root,lst):
            if root == None:
                return
            collect(root.left,lst)
            lst.append(root.val)
            collect(root.right,lst)
        def traverse(root,sums):
            if root==None:
                return
            lst = []
            collect(root,lst)
            sums.append(sum(lst))
            traverse(root.left,sums)
            traverse(root.right,sums)
        traverse(root,sums)
        return max(sums, key=sums.count)
