side_square = int(input('Введите размер стороны квадрата: '))


def square():
    perimeter_diagonal_square = []
    perimeter_diagonal_square.append(side_square*4)
    perimeter_diagonal_square.append((2 ** 0.5) * side_square)
    perimeter_diagonal_square.append(side_square*2)
    return tuple(perimeter_diagonal_square)


print(square())
