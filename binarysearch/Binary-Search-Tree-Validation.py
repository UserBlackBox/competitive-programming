# https://binarysearch.com/problems/Binary-Search-Tree-Validation

class Solution:
    @staticmethod
    def getAll(root,lst):
        if root == None:
            return
        lst.append(root.val)
        Solution.getAll(root.left,lst)
        Solution.getAll(root.right,lst)
    
    def solve(self, root) -> bool:
        if root == None:
            return True
            
        if root.left != None:
            if root.left.val >= root.val:
                return False
            
            if root.left.left != None or root.left.right != None:
                if not self.solve(root.left):
                    return False
                    
            lst = []
            Solution.getAll(root.left,lst)
            if not all(x<root.val for x in lst):
                return False
        
        if root.right != None:
            if root.right.val <= root.val:
                return False

            if root.right.left != None or root.right.right != None:
                if not self.solve(root.left):
                    return False

            lst = []
            Solution.getAll(root.right,lst)
            if not all(x>root.val for x in lst):
                return False

        return True
