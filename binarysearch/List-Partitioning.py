# https://binarysearch.com/problems/List-Partitioning

class Solution:
    def solve(self, strs):
        red = 0
        green = 0
        blue = 0
        for i in strs:
            if i == 'red':
                red += 1
            if i == 'green':
                green += 1
            if i == 'blue':
                blue += 1
        strs = []
        for i in range(red):
            strs.append("red")
        for i in range(green):
            strs.append("green")
        for i in range(blue):
            strs.append("blue")
        return strs
