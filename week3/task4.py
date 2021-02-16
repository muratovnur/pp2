a = input().split()
for x in a:
    if x == '0':
        a.append(a.pop(a.index(x)))
for x in a:
    print(x, end=" ")