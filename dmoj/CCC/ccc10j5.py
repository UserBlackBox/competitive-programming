# https://dmoj.ca/problem/ccc10j5
# https://dmoj.ca/submission/3074640

def valid(x,y):
    return 1 <= x <= 8 and 1 <= y <= 8

start = tuple(map(int,input().split()))
end = tuple(map(int,input().split()))
moves = 0
visited = set()
visit = [start]
while True:
    found = False
    temp = []
    for i in visit:
        if i[0] == end[0] and i[1] == end[1]:
            found = True
            break
        visited.add(i)
        if valid(i[0]-2,i[1]+1) and (i[0]-2,i[1]+1) not in visited:
            temp.append((i[0]-2,i[1]+1))
        if valid(i[0]-2,i[1]-1) and (i[0]-2,i[1]-1) not in visited:
            temp.append((i[0]-2,i[1]-1))
        if valid(i[0]+2,i[1]+1) and (i[0]+2,i[1]+1) not in visited:
            temp.append((i[0]+2,i[1]+1))
        if valid(i[0]+2,i[1]-1) and (i[0]+2,i[1]-1) not in visited:
            temp.append((i[0]+2,i[1]-1))
        if valid(i[0]+1,i[1]-2) and (i[0]+1,i[1]-2) not in visited:
            temp.append((i[0]+1,i[1]-2))
        if valid(i[0]-1,i[1]-2) and (i[0]-1,i[1]-2) not in visited:
            temp.append((i[0]-1,i[1]-2))
        if valid(i[0]+1,i[1]+2) and (i[0]+1,i[1]+2) not in visited:
            temp.append((i[0]+1,i[1]+2))
        if valid(i[0]-1,i[1]+2) and (i[0]-1,i[1]+2) not in visited:
            temp.append((i[0]-1,i[1]+2))
        
    if found:
        break
    moves += 1
    visit = temp

print(moves)

