shopping_list = [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]


shopping_list.sort(key=lambda x: x[1])

print(shopping_list)