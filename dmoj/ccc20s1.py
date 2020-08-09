# https://dmoj.ca/problem/ccc20s1
# https://dmoj.ca/submission/2226272

import sys
n = int(sys.stdin.readline()[:-1])
positions = []
for i in range(n):
    positions.append(tuple(map(int,sys.stdin.readline().split())))
def returnFirst(e):
    return e[0]
positions.sort(key=returnFirst)
largest = 0.0
for i in range(1,n):
    speed = float(abs(positions[i][1]-positions[i-1][1]))/(positions[i][0]-positions[i-1][0])
    largest = max(largest,speed)
print(largest)