# https://dmoj.ca/problem/dmopc18c5p3
# https://dmoj.ca/submission/2946831

from bisect import bisect_left
n,m = tuple(map(int,input().split()))
crayons = list(map(int,input().split()))
for i in range(1,n):
    crayons[i] += crayons[i-1]

longest = 0

if crayons[0] < m:
    right = bisect_left(crayons, crayons[0]+m)
    if crayons[right-1] < m:
        longest = right

for i in range(1,n):
    if crayons[i]-crayons[i-1] >= m:
        continue
    right = bisect_left(crayons, crayons[i-1]+m)
    if crayons[right-1]-crayons[i-1] < m:
        if right-i > longest:
            longest = right-i;
    
print(longest)
