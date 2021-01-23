# https://binarysearch.com/problems/Merging-Binary-Trees

class Solution:
    def solve(self, node0, node1):
        if node0 == None:
            return node1
        if node1 == None:
            return node0
        
        def merge(root0,root1):
            if root0 == None or root1 == None:
                return
            
            if root0.left == None:
                root0.left = root1.left
            elif root1.left != None:
                root0.left.val += root1.left.val
                merge(root0.left,root1.left)
            
            if root0.right == None:
                root0.right = root1.right
            elif root1.right != None:
                root0.right.val += root1.right.val
                merge(root0.right,root1.right)
        
        node0.val += node1.val
        merge(node0,node1)
        return node0
