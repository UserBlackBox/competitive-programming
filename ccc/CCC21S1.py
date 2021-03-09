#!/usr/bin/env python3
from sys import stdin

n = int(stdin.readline())
lengths = list(map(int, stdin.readline().split()))
widths = list(map(int, stdin.readline().split()))
area = 0
for i in range(n):
    area += widths[i]*min(lengths[i], lengths[i+1]) + 0.5*widths[i]*(max(lengths[i], lengths[i+1])-min(lengths[i], lengths[i+1]))
print(area)
