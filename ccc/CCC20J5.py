#!/usr/bin/python3
#ccc 2020 junior 6/15

import sys
grid = []
m = int((sys.stdin.readline()[:-1]))
n = int((sys.stdin.readline()[:-1]))
for i in range(m):
    grid.append(list(map(int,(sys.stdin.readline()[:-1].split()))))

coor = [[m,n]]
found = False

while(True):
    if [1,1] in coor:
        found = True
        break
    newCoor = []
    for a in coor:
        product = a[0]*a[1]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == product: newCoor.append([i+1,j+1])
    coor = newCoor
    if coor == [] or coor == None: break

if found == False: print("no")
else: print("yes")
    
