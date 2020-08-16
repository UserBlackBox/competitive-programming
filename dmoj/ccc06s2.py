# https://dmoj.ca/problem/ccc06s2
# https://dmoj.ca/submission/2225729

import sys
cipher = {}
plaintext = sys.stdin.readline()[:-1]
ciphertext = sys.stdin.readline()[:-1]
for i in range(len(ciphertext)):
    cipher[ciphertext[i]] = plaintext[i]
message = sys.stdin.readline()[:-1]
for i in message:
    try:
        print(cipher[i],end='')
    except KeyError:
        print('.',end='')
print()
