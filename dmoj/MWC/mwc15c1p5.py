# https://dmoj.ca/problem/mwc15c1p5
# https://dmoj.ca/submission/3007270
# written for pypy2

name1 = raw_input().lower()
name2 = raw_input().lower()

chars = 'abcdefghijklmnopqrstuvwxyz'

exponents = [
    [0,0,0,0,0],
    [1,1,1,1,1],
    [6,2,4,8,6],
    [1,3,9,7,1],
    [6,4,6,4,6],
    [5,5,5,5,5],
    [6,6,6,6,6],
    [1,7,9,3,1],
    [6,8,4,2,6],
    [1,9,1,9,1]
]

n1 = 0
n2 = 0
for i in range(len(name1)):
    n1 += exponents[(chars.index(name1[i])+1)%10][(i+1)%4]
for i in range(len(name2)):
    n2 += exponents[(chars.index(name2[i])+1)%10][(i+1)%4]

n1 = n1%10
n2 = n2%10
if n1 == 0: n1 = 10
if n2 == 0: n2 = 10
print n1+n2

