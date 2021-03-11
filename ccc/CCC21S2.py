#!/usr/bin/env python3
#ccc 2021 senior 10/15

from sys import stdin
from itertools import repeat

m = int(stdin.readline())
n = int(stdin.readline())
k = int(stdin.readline())
canvas = []
for _ in range(m):
    canvas.append(list(repeat(False,n)))
gold = 0
for _ in range(k):
    query = stdin.readline().split()
    query[1] = int(query[1])
    if query[0] == 'R':
        for i in range(n):
            if canvas[query[1]-1][i]:
                gold -= 1
            else:
                gold += 1
            canvas[query[1]-1][i] = not canvas[query[1]-1][i]
    if query[0] == 'C':
        for i in range(m):
            if canvas[i][query[1]-1]:
                gold -= 1
            else:
                gold += 1
            canvas[i][query[1]-1] = not canvas[i][query[1]-1]
print(gold)
