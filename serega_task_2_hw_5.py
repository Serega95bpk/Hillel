spisok = str(input('Список продуктов: ')) # Вводим наш список продуктов через запятую (bear, milk, eg, eg, eg, eg)
spisok = list(spisok.split(', ')) # Создаем список из строки и делим его по запятой и пробелу
while 'eg' in spisok: # Проверяем наличе eg в списке если есть в списке то удаляем если нету то выводим список
    spisok.remove('eg')
else:
    print(spisok)
