import math
p = 0.0
q = 0
for i in range(1, 20, 2):
    if q % 2 == 0:
        p += 4.0/i
    else:
        p -= 4.0/i
    q += 1
print(p)
