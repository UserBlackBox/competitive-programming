#!/usr/bin/python3
p = int(input())
n = int(input())
r = int(input())
next = n
n = 0
day = 0
while n<p:
    n += next
    if n>p: break
    next = next*r
    day += 1
print(day)
