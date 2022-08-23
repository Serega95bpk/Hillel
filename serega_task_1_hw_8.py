num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))


def max_num(number_1, number_2, number_3):
    num_list = [number_1, number_2, number_3]
    num_list.sort()
    return f"Наибольшее число: {num_list[-1]}"

print(max_num(num_1, num_2, num_3))