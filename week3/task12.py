a = input().split()
b = input().split()
cnt = 0
for i in a:
    if i in b:
        cnt += 1
print(cnt)