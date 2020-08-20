# https://dmoj.ca/problem/ccc07j1
# https://dmoj.ca/submission/1744054

a = int(input())
b = int(input())
c = int(input())
if (a>c and a<b) or (a<c and a>b): print(a)
elif (b>c and b<a) or (b<c and b>a): print(b)
else: print(c)
