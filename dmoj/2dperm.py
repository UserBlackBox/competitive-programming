# https://dmoj.ca/problem/2dperm
# https://dmoj.ca/submission/2952362
# written for pypy2

from sys import stdin

n,m,q = tuple(map(int,stdin.readline().split()))
diff = [0]*(n*m+2)
for i in range(1,n+1):
    for j in range(1,m+1):
        lo = i*j
        hi = n*m - (n-i+1)*(m-j+1)+1
        diff[lo] += 1
        diff[hi+1] += -1
for i in range(1,len(diff)):
    diff[i] += diff[i-1]

for i in range(q):
    print diff[int(stdin.readline())]

