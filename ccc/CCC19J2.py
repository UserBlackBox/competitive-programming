length = int(input())
i = length
out = []
while i > 0:
    inp = input()
    inp = [str(inp) for inp in inp.split(' ')]
    out.append(str(inp[1] * int(inp[0])))
    i = i - 1

i = 0
while i < length:
    print(out[i])
    i = i + 1