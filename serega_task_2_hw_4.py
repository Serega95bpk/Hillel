stroka_1 = str(input())
d = {}
for b in stroka_1:
    if b in d:
        d[b] += 1
    else:
        d[b] = 1
print(d)


