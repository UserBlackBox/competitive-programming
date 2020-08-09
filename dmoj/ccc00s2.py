# https://dmoj.ca/problem/ccc00s2
# https://dmoj.ca/submission/2609680

import sys
n = int(sys.stdin.readline())
streams = []
for i in range(n):
    streams.append(int(sys.stdin.readline()))

while True:
    temp = sys.stdin.readline()[:-1]
    if temp == '77':
        break
    elif temp == '88':
        idx = int(sys.stdin.readline())-1
        streams[idx] += streams[idx+1]
        streams = streams[:idx+1] + streams[idx+2:]
    elif temp == '99':
        idx = int(sys.stdin.readline())-1
        flow = streams[idx]
        percent = int(sys.stdin.readline())/100
        streams[idx] = flow*percent
        streams.insert(idx+1,flow*(1.0-percent))

print(' '.join(list(map(lambda e: str(int(e)),streams))))