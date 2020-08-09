# https://dmoj.ca/problem/ccc18s1
# https://dmoj.ca/submission/2226251

import sys
import itertools
n = int(sys.stdin.readline()[:-1])
villages = []
for i in range(n,0,-1):
    villages.append(int(sys.stdin.readline()[:-1]))
villages.sort()

sizes = []
for i in range(1,len(villages)-1):
    size = ((villages[i]+villages[i+1])/2.0)-((villages[i]+villages[i-1])/2.0)
    sizes.append(size)
print(min(sizes))