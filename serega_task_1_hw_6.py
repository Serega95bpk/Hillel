first = {1: 10, 2: 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}
fourth = {7: 70, 8: 80}
fifth = {9: 90, 10: 100}
merged_dict = {}

#################################################

for key, value in first.items():
    merged_dict[key] = value

for key, value in second.items():
    merged_dict[key] = value

for key, value in third.items():
    merged_dict[key] = value

for key, value in fourth.items():
    merged_dict[key] = value

for key, value in fifth.items():
    merged_dict[key] = value

print(merged_dict)

########################################################

first.update(second)
first.update(third)
first.update(fourth)
first.update(fifth)

print(first)

#########################################################

merged_dict = {**first, **second, **third, **fourth, **fifth}

print(merged_dict)

#########################################################

merged_dict = first | second | third | fourth | fifth

print(merged_dict)

#########################################################