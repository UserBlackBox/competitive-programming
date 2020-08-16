# https://dmoj.ca/problem/hkccc08j3
# https://dmoj.ca/submission/2609431

contacts = {}
for i in range(int(input())):
    temp = input().split()
    contacts[temp[0]] = temp[1]

calls = {}
for i in range(int(input())):
    temp = input()
    try:
        calls[temp] += 1
    except KeyError:
        calls[temp] = 1

number = list(calls.keys())[0]
for phone, num in calls.items():
    if num > calls[number]:
        number = phone
    elif num == calls[number]:
        number = str(min(int(phone),int(number)))

for name, num in contacts.items():
    if num == number:
        print(name)
        break