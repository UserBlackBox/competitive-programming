# https://dmoj.ca/problem/pwindsor18p7
# https://dmoj.ca/submission/2243834

import sys
import itertools
from functools import cmp_to_key
n = int(sys.stdin.readline())
nums = []
for i in itertools.repeat(None,n):
    nums.append(sys.stdin.readline()[:-1])

def cmp(a,b):
    if int(a) == int(b):
        return 0
    if int(a+b) < int(b+a):
        return 1
    else:
        return -1

nums.sort(key=cmp_to_key(cmp))

print(''.join(nums))