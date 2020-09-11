# https://dmoj.ca/problem/ccc05j5
# https://dmoj.ca/submission/3008291

from sys import stdin

def monkeyTest(word) -> bool:
    legit = False
    if len(word) == 0:
        return False
    if word[0] == "B" and word[-1] == "S" and not legit:
        legit = monkeyTest(word[1:-1])
    if "N" in word and not legit:
        for i in range(len(word)):
            if word[i] != "N":
                continue
            if all([monkeyTest(word[:i]), monkeyTest(word[i+1:])]):
                legit = True
                break
    
    if word == "A":
        return True
    return legit

while True:
    word = stdin.readline()[:-1]
    if word == "X":
        break
    if monkeyTest(word) == True:
        print("YES")
    else:
        print("NO")

