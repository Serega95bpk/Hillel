my_dict = {}

for x in range(11, 21):
    my_dict[x] = x**2
print(my_dict)

sum_dict = sum(my_dict.values())
print(sum_dict)