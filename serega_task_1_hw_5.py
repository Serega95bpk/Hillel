new_pass = str(input('Введите новый пароль: '))
confirm_pass = str(input('Подтвердите пароль: '))
while new_pass != confirm_pass: # Проверяем сходятся ли пароли если нет то запрашиваем ввести пароль заного, если сходятся то выводим приветствие
    confirm_pass = str(input('Пароли не совпадают. Повторите пароль: '))
else:
    print('Добро пожаловать!')