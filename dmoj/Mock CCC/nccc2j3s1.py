# https://dmoj.ca/problem/nccc2j3s1
# https://dmoj.ca/submission/3002361

from sys import stdin
n = int(stdin.readline())
s = 0
nums = []
m = 0
for i in range(n):
    nums.append(int(stdin.readline()))
    s += nums[-1]
    m = max(nums[-1],m)
print(min(s-m,s//2))

