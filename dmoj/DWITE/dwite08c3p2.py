# https://dmoj.ca/problem/dwite08c3p2
# https://dmoj.ca/submission/2193645

for n in range(5):
    line = list(input())
    for i in range(len(line)):
        if not (ord(line[i])==32 or (ord(line[i])>=65 and ord(line[i])<=90) or (ord(line[i])>=97 and ord(line[i])<=122)):
            line[i] = ' '
    line = "".join(line)
    line = line.split()
    words = 0
    for i in line:
        if len(i)>3:
            words+=1
    print(words)
