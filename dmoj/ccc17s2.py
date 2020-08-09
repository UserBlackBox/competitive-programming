# https://dmoj.ca/problem/ccc17s2
# https://dmoj.ca/submission/2208088

import itertools
n = int(input())
records = sorted(list(map(int,input().split())))
if n%2==0:
    mid = n//2
else:
    mid = n//2+1
low = records[:mid]
low.reverse()
high = records[mid:]
records = [x for x in itertools.chain.from_iterable(itertools.zip_longest(low,high)) if x]
print(" ".join(list(map(str, records))))