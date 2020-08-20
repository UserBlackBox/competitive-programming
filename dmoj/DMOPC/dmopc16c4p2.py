# https://dmoj.ca/problem/dmopc16c4p2
# https://dmoj.ca/submission/2202879

import bisect

batches = []
for i in range(int(input())):
    batches.append(list(map(int, input().split())))
fails = []
for i in range(int(input())):
    fails.append(int(input()))
fails.sort()
points = 0
for i in batches:
    left = bisect.bisect_left(fails,i[0])
    try:
        batch_fails = fails[left]
        if batch_fails>=i[0] and batch_fails<=i[1]:
            pass
        else:
            points += i[2]
    except IndexError:
        points += i[2]
print(points)