# https://dmoj.ca/problem/gfssoc2j5
# https://dmoj.ca/submission/2952302

from sys import stdin
n,q = tuple(map(int,stdin.readline().split()))
episodes = [0]+list(map(int,stdin.readline().split()))

pmax = [0]
pmax_count = [0]
for i in range(n):
    if episodes[i+1] > pmax[-1]:
        pmax.append(episodes[i+1])
        pmax_count.append(1)
    elif episodes[i+1] == pmax[-1]:
        pmax.append(episodes[i+1])
        pmax_count.append(pmax_count[-1]+1)
    else:
        pmax.append(pmax[-1])
        pmax_count.append(pmax_count[-1])

smax = [episodes[-1]]
smax_count = [1]
for i in range(n-1,0,-1):
    if episodes[i] > smax[-1]:
        smax.append(episodes[i])
        smax_count.append(1)
    elif episodes[i] == smax[-1]:
        smax.append(episodes[i])
        smax_count.append(smax_count[-1]+1)
    else:
        smax.append(smax[-1])
        smax_count.append(smax_count[-1])
smax.reverse()
smax_count.reverse()
smax = smax + [0]
smax_count = smax_count + [0]

for i in range(q):
    query = tuple(map(int,stdin.readline().split()))
    if pmax[query[0]-1] == smax[query[1]]:
        print(pmax[query[0]-1],end=' ')
        print(pmax_count[query[0]-1] + smax_count[query[1]])
    elif pmax[query[0]-1] > smax[query[1]]:
        print(pmax[query[0]-1],end=' ')
        print(pmax_count[query[query[0]-1]])
    else:
        print(smax[query[1]],end=' ')
        print(smax_count[query[1]])

