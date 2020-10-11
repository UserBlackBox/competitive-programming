# https://dmoj.ca/problem/coci14c2p2
# https://dmoj.ca/submission/3058948

from sys import stdin

n = int(stdin.readline())
runners = dict()
for i in range(n):
    runner = stdin.readline()
    if runner in runners:
        runners[runner] += 1
    else:
        runners[runner] = 1
for i in range(n-1):
    runner = stdin.readline()
    runners[runner] -= 1
    if runners[runner] == 0:
        del runners[runner]
print(next(iter(runners))[:-1])


