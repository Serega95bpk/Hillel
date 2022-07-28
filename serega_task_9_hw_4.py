list_1: list = (1, 2, 3, 4, 5, 6)
list_2: list = ('a', 'b', 'j', 1, 'e')

for x in list_1:
    if x in list_2:
        print(bool(x))