# https://dmoj.ca/problem/dmopc17c5p3
# https://dmoj.ca/submission/3078739

from math import sqrt
from fractions import gcd
raw_input()
nums = list(map(int, raw_input().split()))
gcd = reduce(gcd, nums)
ans = 0
while gcd%2 == 0:
    ans = 2
    gcd = gcd/2
for i in range(3, int(sqrt(gcd))+1, 2):
    while gcd%i==0:
        ans = i
        gcd = gcd/i
if gcd > 2:
    ans = gcd
if ans == 0:
    print "DNE"
else:
    print int(ans)

