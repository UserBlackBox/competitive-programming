# https://dmoj.ca/problem/tree1
# https://dmoj.ca/submission/3061014

from sys import exit

matrix = []
for i in range(4):
    matrix.append([])
    temp = list(map(int,input().split()))
    for j in temp:
        matrix[-1].append(bool(j))

#undirection check
for i in range(4):
    for j in range(4):
        if matrix[i][j] != matrix[j][i]:
            print("No")
            exit(0)

#connectedness check
checked = [False,False,False,False]
search = [0]
for i in range(4):
    temp = []
    for j in search:
        checked[j] = True
        for x in range(4):
            if matrix[j][x]:
                temp.append(x)
    search = temp
if not all(checked):
    print("No")
    exit(0)

search = [(-1,0)]
checked = [False,False,False,False]
while True:
    temp = []
    for i in search:
        checked[i[1]] = True
        for x in range(4):
            if x == i[0]:
                continue
            if matrix[i[1]][x] and checked[x]:
                print("No")
                exit(0)
            if matrix[i[1]][x]:
                temp.append((i[1],x))
    search = temp
    if all(checked): break
print("Yes")

