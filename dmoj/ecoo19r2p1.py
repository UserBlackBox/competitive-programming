# https://dmoj.ca/problem/ecoo19r2p1
# https://dmoj.ca/submission/2193721

for c in range(10):
    n = int(input())
    addresses = set([])
    for i in range(n):
        address = input()
        address = address.lower()
        address = address.split('@')
        address[0] = address[0].split('+')
        address[0] = address[0][0]
        address[0] = address[0].replace('.','')
        address = '@'.join(address)
        addresses.add(address)
    print(len(addresses))