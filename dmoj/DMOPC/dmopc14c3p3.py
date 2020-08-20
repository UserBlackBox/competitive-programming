# https://dmoj.ca/problem/dmopc14c3p3
# https://dmoj.ca/submission/2226383

import sys
import bisect
n = int(sys.stdin.readline())
veterans = []
for i in range(n):
    veterans.append(sys.stdin.readline()[:-1].split())
    veterans[i][1] = int(veterans[i][1])

def returnSecond(e):
    return e[1]

veterans.sort(key=returnSecond)
q = int(sys.stdin.readline())
skills = [x[1] for x in veterans]
for i in range(q):
    new = list(map(int,sys.stdin.readline().split()))
    left = bisect.bisect_left(skills,new[0])
    if left == len(skills):
        print('No suitable teacher!')
        continue
    if skills[left] <= new[0]+new[1]:
        print(veterans[left][0])
    else:
        print('No suitable teacher!')