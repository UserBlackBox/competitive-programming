# https://dmoj.ca/problem/dmopc18c2p4
# https://dmoj.ca/submission/2948484

from sys import exit
n,m = tuple(map(int,input().split()))
damage = list(map(int,input().split()))
for i in range(1,n):
    damage[i] += damage[i-1]

if damage[-1] < m:
    print(-1)
    exit(0)

shortest = n
damage = [0]+damage

i = 0
j = 1
while i < n+1 > j:
    if damage[j] - damage[i] < m:
        j+=1
    else:
        i+=1
        shortest = min(shortest,j-i)
print(shortest+1)
