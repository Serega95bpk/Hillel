stroka_1 = str(input())
if len(stroka_1) < 2:
    stroka_2 = str('Ваша строка слишком короткая - %s') % stroka_1
    print(stroka_2)
else:
    stroka_3 = stroka_1[:2] + stroka_1[-2:]
    print(stroka_3)
