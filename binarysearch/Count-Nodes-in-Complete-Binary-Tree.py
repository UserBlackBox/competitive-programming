# https://binarysearch.com/problems/Count-Nodes-in-Complete-Binary-Tree

class Solution:
    @staticmethod
    def getList(root, lst):
        if root == None: return
        else:
            lst.append(root.val)
            Solution.getList(root.left, lst)
            Solution.getList(root.right, lst)

    def solve(self, root):
        lst = []
        Solution.getList(root, lst)
        return len(lst)

