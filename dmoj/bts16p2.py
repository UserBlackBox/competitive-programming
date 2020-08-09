# https://dmoj.ca/problem/bts16p2
# https://dmoj.ca/submission/2429139

s = []
n = int(input())
for i in range(n):
    temp = input().split()
    if temp[0] == '1':
        if temp[1] in s:
            print('false')
            continue
        s.append(temp[1])
        print('true')
    elif temp[0] == '2':
        if temp[1] not in s:
            print('false')
            continue
        s.remove(temp[1])
        print('true')
    elif temp[0] == '3':
        try:
            print(s.index(temp[1]))
        except ValueError:
            print(-1)
    elif temp[0] == '4':
        print(' '.join(sorted(s)))