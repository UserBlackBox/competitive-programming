# https://dmoj.ca/problem/tle17c2p2
# https://dmoj.ca/submission/2226299

import sys
import bisect
import itertools
k = int(sys.stdin.readline()[:-1])
unlucky = sorted(list(map(int,sys.stdin.readline()[:-1].split())))
n = int(sys.stdin.readline()[:-1])
for i in itertools.repeat(None,n):
    building = int(sys.stdin.readline()[:-1])
    idx = bisect.bisect_right(unlucky,building)
    print(building-idx)