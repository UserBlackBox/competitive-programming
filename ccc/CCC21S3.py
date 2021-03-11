#!/usr/bin/env python3
#ccc 2021 senior 4/15

from sys import stdin, exit

n = int(stdin.readline())
friends = []
friends.append(tuple(map(int, stdin.readline().split())))
maxP = friends[0][0]
minP = friends[0][0]
for _ in range(n-1):
    friends.append(tuple(map(int, stdin.readline().split())))
    minP = min(minP, friends[-1][0])
    maxP = max(maxP, friends[-1][0])

if n == 1:
    print(0)
    exit(0)

minM = -1
for c in range(minP, maxP+1):
    minutes = 0
    for friend in friends:
        if friend[0]-friend[2] <= c <= friend[0]+friend[2]:
            continue
        else:
            if c < friend[0]-friend[2]:
                minutes += ((friend[0]-friend[2])-c)*friend[1]
            else:
                minutes += (c-(friend[0]+friend[2]))*friend[1]
    if minM == -1:
        minM = minutes
    elif minutes < minM:
        minM = minutes
print(minM)
