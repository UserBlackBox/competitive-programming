# https://dmoj.ca/problem/ccc08j4
# https://dmoj.ca/submission/2609708

import sys
while True:
    line = sys.stdin.readline()[:-1].split()
    if line == ['0']:
        break
    postfix = []
    line = line[::-1]
    for i in line:
        if i == '+' or i == '-':
            a = postfix.pop()
            b = postfix.pop()
            postfix.append(a+' '+b+' '+i)
        else:
            postfix.append(i)
    print(' '.join(postfix))