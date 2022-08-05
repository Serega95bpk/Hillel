dict_name = {'id1': { 'name': 'Ruslan', 'class': 1, 'subjects': {'Math', 'Algorithms', 'English'}},
             'id2': {'name': 'Mark', 'class': 2, 'subjects': {'Geometry', 'Java', 'Cooking'}},
             'id3': {'name': 'Ruslan', 'class': 1, 'subjects': {'Math', 'Algorithms', 'English'}}}
dict_name_new = {}

for key, value in dict_name.items():
    if value not in dict_name_new.values():
        dict_name_new.update({key: value})
print(dict_name_new)

