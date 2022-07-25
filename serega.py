
##########################################################
# 1. Примеры методов строк.
##########################################################
method1: str = 'google'
x = method1.capitalize()
print(x)
###################################
method2: str = 'Google'
x = method2.lower()
print(x)
###################################
method3: str = 'Google'
x = method3.casefold()
print(x)
###################################
method4: str = 'Google'
x = method4.center(22, "$")
print(x)
###################################
method5: str = 'GoogleGoogleGoogleGoogleGoogleGoogleGoogleGoogleGoogle'
x = method5.count("oo", 2, 28)
print(x)
###################################
method6: str = 'Google'
x = method6.encode(encoding = 'utf_32', errors = 'ignore' )
print(x)
###################################
method7: str = 'Google'
x = method7.endswith('le')
y = method7.endswith('ds')
print(x, y)
###################################
method8: str = '1\t233\t333333\t3331\t456\t64908'
x = method8.expandtabs(15)
print(x)
##################################
method9: str = '1234567890'
x = method9.find('5')
print(x)
##################################
method10: str = 'карма: {0}, рейтинг: {1}, имя - {name}, ник - {nik_name}'
z: str = 'Serega'
v: str = 'Profi'
x = method10.format(54, 985, name = z, nik_name = v)
print(x)
##################################
method11: str = '1234567890'
x = method11.index('5')
print(x)
##################################
method9: str = '1234567890'
x = method9.isalnum()
print(x)
#################################
method12: str = '1234567890'
x = method12.isalpha()
print(x)
################################
method13: str = '1234567890'
x = method13.isdecimal()
print(x)
################################
method14: str = '1234567890'
x = method14.isdigit()
print(x)
################################
method15: str = 'Google'
x = method15.isidentifier()
print(x)
###############################
method16: str = '\u00be'
print(method16)
x = method16.isnumeric()
print(x)
###############################
method17: str = '\u001c'
print(method17)
x = method17.isnumeric()
print(x)
################################
method18: str = '    '
x = method18.isspace()
print(x)
################################
method19: str = 'Google'
x = method19.istitle()
print(x)
################################
method20: str = 'GOOGLE'
x = method20.isupper()
print(x)
################################
method21: str = ', '
x = method21.join(['1', '2', '3'])
print(x)
###############################
method22: str = 'KLL'
x = method22.ljust(8, 'D')
print(x)
###############################
method23: str = 'GOOGLE'
x = method23.lower()
print(x)
###############################
method24 = ''.maketrans('abc', '123')
x = 'a+b=c'.translate(method24)
print(x)
################################
method25: str = 'GOOGLE.gmail.com'
x = method25.partition('.gmail')
print(x)
###############################
method26: str = 'QWERTY12345'
x = method26.replace('QWERTY', 'ADMIN')
print(x)
###############################
method27: str = 'qwertyjsdkasd'
x = method27.rfind('k')
print(x)
##############################
method28: str = 'qwertyjsdkasd'
x = method28.rindex('a')
print(x)
###############################
method29: str = 'ASD'
x = method29.rjust(6, 'k')
print(x)
###############################
method30: str = 'qwejrtyjsdkasd'
x = method30.rpartition('j')
print(x)
###############################
method31: str = 'qwertyjsdkasd'
x = method31.rsplit('k')
print(x)
###############################
method32: str = 'qwekrtykjsdkasd'
x = method32.rstrip('dsa')
print(x)
################################
method33: str = '1 2 3 4 5'
x = method33.split()
print(x)
################################
method34: str = 'qwekrtykjsdkasd'
x = method34.startswith('qwe')
print(x)
################################
method35: str = 'aaaSSSaaa'
x = method35.strip('aaa')
print(x)
################################
method36: str = 'aaaSSSaaa'
x = method36.swapcase()
print(x)
################################
method37: str = 'hELLO wOrLd'
x = method37.title()
print(x)
################################
method38: str = 'google'
x = method38.upper()
print(x)
################################
method39: str = 'aaaSSSaaa'
x = method39.strip('aaa')
print(x)
################################
method40: str = 'aaa'
x = method40.zfill(7)
print(x)

##############################################
#  2. По 3 варинта всех уже изученных объектов в Пайтоне.
##############################################
String_1: str = 'Как тебя зовут?'
String_2: str = 'Сколько тебе лет?'
String_3: str = '''Целое, целочисленный тип данных — один из самых\nпростых примитивных типов данных.
Служит для представления целых чисел,\tограниченного\tминимальным и максимальным значением, 
зависящими от выделенной под число памяти.'''
print(String_1)
print(String_2)
print(String_3)
##############################################
x1: int = 12
x2: int = 89
x3: int = 159
x4: float = 9.63
x5: float = 74.657
x6: float = 678.9453
##################################################
my_list_1 = [1, 2, 3]
my_list_1[1] = 11
my_list_1[2] = 26
print(my_list_1)

my_list_2 = [1, 2, 3, 4, 5]
del my_list_2 [1]
del my_list_2 [:2]
del my_list_2 [:]
print(my_list_2)

a = [3, 2, 1]
b = [1, 2, 3]
d = [3, 2, 2]
e = [3, 2]
f = [3, 2, 'a']
a > b  # True
a > d  # False
d > b  # True
a > e  # True
##############################################
d = dict([(1, 1), (2, 4)])
print(d)

v = {a: a ** 2 for a in range(7)}
print(v)

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic1.update(dic2)
print(dic1)
##############################################
a1 = (1, 2, 3, 4, 5, 6)
print(a1)

a2 = ('a', 'b', 'c', 'd')
print(a2)

a3 = tuple('hello, world!')
print(a3)
##############################################
# 3. Написать 3 примера использования max(), min()
##############################################
b1 = [11, 8, 12, 0]
c1 = min(b1)
print(c1)

b2 = [11, 8, 12, 0]
c2 = max(b2)
print(c2)

b3 = [11, 8, 12, 0]
b4 = [11, 7, 123, 9, 78]
c3 = min(b3, b4)
print(c3)
##############################################
# 4. Написать 3 примера различных с оператором in.
##############################################
e1 = 'me' in 'disappointment'
print(e1)

pets = ['собака', 'кот', 'сова']
e2 = 'собака' in pets
print(e2)

e3 = 'pot' not in 'disappointment'
print(e3)
##############################################
# 5. Написать 3 примера условия if elif else.
##############################################
number = int(input("Введите число: "))
if number > 10:
    print("Число больше 10")
elif number < 10:
    print("Число меньше 10")
else
    print("Число равно 10")


score = int(input("Введите вашу оценку: "))
if score >= 90:
    print("Отлично! Ваша оценка А")
elif score >= 80:
    print("Здорово! Ваша оценка - B")
elif score >= 70:
    print("Хорошо! Ваша оценка - C")
elif score >= 60:
    print("Ваша оценка - D. Стоит повторить материал.")
else:
    print("Вы не сдали экзамен")


gre_score = int(input("Введите текущий лимит: "))
per_grad = int(input("Введите кредитный рейтинг: "))
if per_grad > 70:
    if gre_score > 150:
        print("Поздравляем, вам выдан кредит")
    else:
        print("У вас низкий кредитный лимит")
else:
    print("Извините, вы не имеете права на кредит")
##############################################
