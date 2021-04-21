# https://binarysearch.com/problems/Invert-Tree

class Solution:
    def solve(self, root):
        if root == None: return None
        else:
            left = self.solve(root.right)
            right = self.solve(root.left)
            root.left = left
            root.right = right
        return root
        
