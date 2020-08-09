inp = input()
h = int(inp.count("H"))
v = int(inp.count("V"))
flip_h = False
flip_v = False

if h % 2 == 1:
    flip_h = True

if v % 2 == 1:
    flip_v = True

if flip_h == True and flip_v == True:
    print("4 3")
    print("2 1")
elif False == flip_h and flip_v == True:
    print("2 1")
    print("4 3")
elif flip_h == True and flip_v == False:
    print("3 4")
    print("1 2")
else:
    print("1 2")
    print("3 4")
