# https://dmoj.ca/problem/dwite09c1p3
# https://dmoj.ca/submission/2184915

for i in range(5):
    n = int(input())
    nums = []
    for j in range(n):
        nums.append(int(input()))
    m = 0
    for j in range(1,n+2):
        try:
            nums.index(j)
        except ValueError:
            m = j
            break
    print(m)