# https://dmoj.ca/problem/dmopc17c5p2
# https://dmoj.ca/submission/2950681

from sys import stdin
from itertools import repeat
from bisect import bisect_left
s = stdin.readline()[:-1]
ones = [0]
zeros = [0]
for i in range(len(s)):
    if s[i] == '0':
        zeros.append(1+zeros[-1])
        ones.append(ones[-1])
    else:
        zeros.append(zeros[-1])
        ones.append(1+ones[-1])

q = int(stdin.readline())

for x in repeat(None,q):
    case = tuple(map(int,stdin.readline().split()))
    if case[2] == 1:
        right = bisect_left(ones,case[1]+ones[case[0]-1],lo=case[0])
        if right >= len(ones):
            print(-1)
            continue
        print(right)
    if case[2] == 0:
        right = bisect_left(zeros,case[1]+zeros[case[0]-1],lo=case[0])
        if right >= len(zeros):
            print(-1)
            continue
        print(right)
