list_1 = [1, 2, 3]
list_2 = [11, 22, 33]


def list_gen(list_1, list_2):
 mix_list = zip(list_1, list_2)
 new_list = [i for d in mix_list for i in d]
 return new_list


print(list_gen(list_1, list_2))