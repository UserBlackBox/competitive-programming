# https://dmoj.ca/problem/dwite10c1p1
# https://dmoj.ca/submission/2185737

for a in range(5):
    date = list(map(int,input().split()))

    if date[2] > 1997:
        print('too young')
        continue

    elif date[2] < 1997:
        print('old enough')
        continue

    elif date[2] == 1997:
        if date[1] > 10:
            print('too young')
            continue

        elif date[1] < 10:
            print('old enough')
            continue

        elif date[1] == 10:
            if date[0] <=27:
                print('old enough')
                continue

            else:
                print('too young')
                continue