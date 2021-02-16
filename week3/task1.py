arr = input()
a = arr.split()
for i in range(0, len(a), 2):
    if i % 2 == 0:
        print(a[i], end=" ")