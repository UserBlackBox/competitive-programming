# https://dmoj.ca/problem/fts
# https://dmoj.ca/submission/2192017

size = int(input())
switchboard = list(input())
moves = 0
index = 0

for i in range(1,size):
    if switchboard[i] != switchboard[i-1]:
        moves+=1
        switchboard[i-1] = switchboard[i]

if switchboard[size-1] == '1':
    moves += 1

print(moves)