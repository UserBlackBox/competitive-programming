#!/usr/bin/python3
def shift(text):
    return text[1:] + text[0]

t = input()
s = input()
found = False
for i in range(len(s)):
    if t.find(s) != -1:
        found = True
        break
    s = shift(s)
if found == True: print("yes")
else: print("no")
