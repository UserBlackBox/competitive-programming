#!/usr/bin/env python3
#ccc 2021 senior 4/15

from sys import stdin
from itertools import repeat

n,w,d = map(int, stdin.readline().split())
walkways = {}
for _ in range(w):
    temp = tuple(map(int, stdin.readline().split()))
    if temp[0] in walkways:
        walkways[temp[0]].append(temp[1])
    else:
        walkways[temp[0]] = [temp[1]]
subway = list(map(int, stdin.readline().split()))
for _ in range(d):
    swap = tuple(map(int, stdin.readline().split()))
    subway[swap[0]-1], subway[swap[1]-1] = subway[swap[1]-1], subway[swap[0]-1]
    visited = list(repeat(False,n))
    minute = 0
    train = 0
    visit = [1]
    while True:
        temp = set()
        for station in visit:
            if not visited[station-1]:
                visited[station-1] = True
            if station in walkways:
                for i in walkways[station]:
                    temp.add(i)
            if subway[train] == station and train != n-1:
                temp.add(subway[train+1])
            if train < subway.index(station):
                temp.add(station)
        if train != n-1:
            train += 1
        minute += 1
        if n in temp:
            break
        visit = list(temp)
    print(minute)
