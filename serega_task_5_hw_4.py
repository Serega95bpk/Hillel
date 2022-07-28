stroka_1: str = ('red, white, black, red, green, black')
stroka_1 = stroka_1.split(', ')
stroka_1 = list(stroka_1)
unique = []
for color in stroka_1:
    if color not in unique:
        unique.append(color)
unique.sort()
print(unique)

