# https://dmoj.ca/problem/tss17a
# https://dmoj.ca/submission/2226280

import sys
n = int(sys.stdin.readline()[:-1])
for i in range(n):
    instruction = sys.stdin.readline()[:-1].split()
    printed = False
    for j in range(3):
        if instruction.count(instruction[j]) >= 2:
            print(instruction[j])
            printed = True
            break
    if not printed:
        print('???')