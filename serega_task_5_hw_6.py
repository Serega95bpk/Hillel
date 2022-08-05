my_list = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
########################################
# С основным заданием проблем не возникло
########################################
unique_values = set()
for item in my_list:
     for val in item.values():
          unique_values.add(val)
print(unique_values)

#########################################################
# А вот с дополнительным заданием. Не смог довести его до полноценного конца.
#########################################################


unique_values_2 = []

for item in my_list:
     for val in item.values():
          unique_values_2.append(val)

unique_values_3 = []

for item in unique_values_2:
     if item not in unique_values_3:
          unique_values_3.append(item)

# print(unique_values_3)



unique_keys_1 = []

for item in my_list:
     for val in item.keys():
         unique_keys_1.append(val)

unique_keys_2 = []

for item in unique_keys_1:
     if item not in unique_keys_2:
          unique_keys_2.append(item)

# print(unique_keys_1)

# unique_keys_2 = []
#
# while len(unique_values_3) != len(unique_keys_1):
#      for x in unique_keys_1:
#           unique_keys_2.append(x)
#      break
# print(unique_keys_2)


my_list_2 = [{x:unique_values_3[i]} for i, x in enumerate(unique_keys_2)]

print(my_list_2)

