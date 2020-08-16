# https://dmoj.ca/problem/ccc17s1
# https://dmoj.ca/submission/2204275

n = int(input())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))

day = 0
for i in range(1,n+1):
    a[i] += a[i-1]
    b[i] += b[i-1]
    if a[i] == b[i]:
        day = i

print(day)