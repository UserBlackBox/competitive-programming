# https://binarysearch.com/problems/Column-Sort

class Solution:
    def solve(self, matrix):
        for i in range(len(matrix[0])):
            column = [x[i] for x in matrix]
            column.sort()
            for j in range(len(matrix)):
                matrix[j][i] = column[j]
        return matrix

