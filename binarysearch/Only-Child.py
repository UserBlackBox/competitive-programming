# https://binarysearch.com/problems/Only-Child

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @staticmethod
    def iter(root, num):
        if root == None:
            return
        if root.left != None and root.right != None:
            Solution.iter(root.left,num)
            Solution.iter(root.right,num)
        elif root.left != None and root.right == None:
            num[0] += 1
            Solution.iter(root.left,num)
        elif root.left == None and root.right != None:
            num[0] += 1
            Solution.iter(root.right,num)

    def solve(self, root):
        num = [0]
        Solution.iter(root,num)
        return num[0]

