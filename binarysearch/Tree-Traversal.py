# https://binarysearch.com/problems/Tree-Traversal

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, moves):
        pos = ['root']
        for i in moves:
            if i == 'RIGHT':
                pos.append('.right')
            elif i == 'LEFT':
                pos.append('.left')
            elif i == 'UP':
                pos = pos[:-1]
        pos += '.val'
        return eval(''.join(pos))
