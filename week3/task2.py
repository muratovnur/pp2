a = list(map(int, input().split()))
mini = 1000
for el in a:
    if el > 0 and el < mini:
        mini = el
print(mini)