# https://binarysearch.com/problems/Sudoku-Validator
# https://binarysearch.com/problems/Sudoku-Validator/submissions/1038733

class Solution:
    def solve(self, matrix):
        sudoku_nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
        for i in matrix:  # loop through rows
            if set(i) != sudoku_nums:  # compare rows by sorting
                return False  # if row is invalid then return false
        for i in range(9):  # loop through columns
            column = [
                x[i] for x in matrix
            ]  # create column variable to hold values using comprehension
            if set(column) != sudoku_nums:  # compare columns
                return False
        for i in range(0, 9, 3):  # loop through rows of subgrids
            for j in range(0, 9, 3):  # loop through columns of subgrids
                nums = []
                for x in range(j, j + 3):  # collect values of subgrid
                    nums.append(matrix[i][x])
                    nums.append(matrix[i + 1][x])
                    nums.append(matrix[i + 2][x])
                if set(nums) != sudoku_nums:  # sort and compare
                    return False
        return True  # if passed all checks then grid is valid
