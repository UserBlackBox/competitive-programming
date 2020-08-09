#!/usr/bin/python3
n = int(input())
x = []
y = []
for i in range(n):
    temp = input().split(",")
    if int(temp[0])>0 and int(temp[1])<100: x.append(int(temp[0]))
    if int(temp[1])>0 and int(temp[1])<100: y.append(int(temp[1]))

print(str(min(x)-1) + "," + str(min(y)-1))
print(str(max(x)+1) + "," + str(max(y)+1))
