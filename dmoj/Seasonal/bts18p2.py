# https://dmoj.ca/problem/bts18p2
# https://dmoj.ca/submission/2963170

from sys import stdin
from bisect import bisect_left, bisect_right

sentence = stdin.readline()[:-1]
letters = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [], 'l': [], 'm': [], 'n': [], 'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [], 'u': [], 'v': [], 'w': [], 'x': [], 'y': [], 'z': []}
for i in range(len(sentence)):
    if sentence[i] == ' ':
        continue
    letters[sentence[i]].append(i+1)
q = int(stdin.readline())
for i in range(q):
    temp = stdin.readline().split()
    temp[0] = int(temp[0])
    temp[1] = int(temp[1])
    left = bisect_left(letters[temp[2]],temp[0])
    right = bisect_right(letters[temp[2]],temp[1],lo=left)
    print(right-left)
