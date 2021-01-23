# https://binarysearch.com/problems/Sum-of-Right-Leaves

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    num = 0
    def solve(self, root):
        if root == None:
            return 0
        self.num = 0
        def iter(tree, right):
            if tree.right != None:
                iter(tree.right, True)
            if tree.left != None:
                iter(tree.left, False)
            if right and tree.right == None and tree.left == None:
                self.num += tree.val
        iter(root, False)
        return self.num

