A_Three = int(input())
A_Two = int(input())
A_One = int(input())
B_Three = int(input())
B_Two = int(input())
B_One = int(input())
A = A_Three * 3 + A_Two * 2 + A_One
B = B_Three * 3 + B_Two * 2 + B_One

if A > B:
    print("A")
elif B > A:
    print("B")
elif A == B:
    print("T")