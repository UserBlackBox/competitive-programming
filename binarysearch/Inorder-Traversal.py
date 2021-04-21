# https://binarysearch.com/problems/Inorder-Traversal

class Solution:
    @staticmethod
    def getList(root, lst):
        if root == None: return
        else:
            Solution.getList(root.left, lst)
            lst.append(root.val)
            Solution.getList(root.right, lst)

    def solve(self, root):
        lst = []
        Solution.getList(root, lst)
        return lst

