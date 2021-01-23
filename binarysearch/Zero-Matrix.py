# https://binarysearch.com/problems/Zero-Matrix

class Solution:
    def solve(self, matrix):
        change = []
        for i in range(len(matrix)):
            change.append([False for x in range(len(matrix[i]))])
        for i in range(len(change)):
            for j in range(len(change[i])):
                if 0 in matrix[i] or 0 in [x[j] for x in matrix]:
                    change[i][j] = True
        for i in range(len(change)):
            for j in range(len(change[i])):
                if change[i][j]:
                    matrix[i][j] = 0
        return matrix

