# https://dmoj.ca/problem/seed2
# https://dmoj.ca/submission/2208116


import sys
low = 1
high = 2*10**9
mid = (low+high)//2

while True:
    print(mid)
    sys.stdout.flush()
    status = input()
    if status == 'SINKS':
        low = mid
    if status == 'FLOATS':
        high = mid
    if status == 'OK':
        break
    mid = (low+high)//2
sys.exit(0)