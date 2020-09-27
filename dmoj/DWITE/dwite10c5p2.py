# https://dmoj.ca/problem/dwite10c5p2
# https://dmoj.ca/submission/3036574

from itertools import repeat
from sys import stdin

for z in repeat(None,5):
    r,c,ro = tuple(map(int,stdin.readline().split()))
    rows = list(repeat(False,r))
    columns = list(repeat(False,c))
    for i in repeat(None,ro):
        temp = tuple(map(int,stdin.readline().split()))
        rows[temp[0]-1] = True
        columns[temp[1]-1] = True
    rowCount = rows.count(True)
    total = 0
    for i in range(0,c):
        if not columns[i]:
            total += r-rowCount
    print(total)
