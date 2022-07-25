year_of_birth = input('Введите год рождения ')
if year_of_birth.isalpha():                                 # Проверка буквами или цифрами ввел год.
    year_of_birth = input('Введите год рождения цифрами ')
year_of_birth_2 = int(year_of_birth)                        # Вводим новую переменную для того что бы год был int.
starting_point: int = 2001                                  # Год от которого считается больше или меньше 21 года человеку (2022 - 2001 = 21)
if year_of_birth_2 == starting_point:                       # Если 21 год
    print('You should visit Holland.')
elif year_of_birth_2 < starting_point:                      # Если старше
    print('You should visit Vietnam.')
else:
    print('Travell everywhere.')
