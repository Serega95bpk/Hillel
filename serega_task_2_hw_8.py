num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))


def max_num_1(number_1, number_2):
    num_list = [number_1, number_2]
    num_list.sort()
    return num_list[-1]


def max_num_2(number_1, number_2, number_3):
    num_max_iz_2 = max_num_1(number_1, number_2)
    num_max_iz_3 = max_num_1(num_max_iz_2, number_3)
    return num_max_iz_3

print(max_num_2(num_1, num_2, num_3))

