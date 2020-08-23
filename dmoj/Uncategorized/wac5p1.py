# https://dmoj.ca/problem/wac5p1
# https://dmoj.ca/submission/2966175
# written for pypy2

n = int(raw_input())
acorns = list(map(int,raw_input().split()))
acorns.sort()
for i in range(n):
    acorns[i] = [acorns[i],acorns[i]]
done = False
while not done:
    done = True
    for i in range(len(acorns)-1,0,-1):
        for j in range(i-1,-1,-1):
            if acorns[j][0] < acorns[i][1]:
                acorns[i][1] = acorns[j][1]
                done = False
                del acorns[j]
                break
        if not done:
            break
s = 0
for i in acorns:
    s+=i[0]
print s

