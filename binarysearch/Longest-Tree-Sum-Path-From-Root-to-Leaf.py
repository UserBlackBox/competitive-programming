# https://binarysearch.com/problems/Longest-Tree-Sum-Path-From-Root-to-Leaf

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root == None:
            return 0
        def traverse(root,length,var,total):
            if root == None:
                if length > var[0]:
                    var.clear()
                    var.append(length)
                    var.append(total)
                if length == var[0]:
                    var.append(total)
                return
            traverse(root.left,length+1,var,total+root.val)
            traverse(root.right,length+1,var,total+root.val)
        
        longest = [0]
        traverse(root,0,longest,0)
        if len(longest) == 2:
            return longest[0]
        else:
            return max(longest[1:])

