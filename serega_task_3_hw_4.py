spisok_1 = ('bread, milk, kolbasa')
spisok_1 = spisok_1.split(', ')
spisok_1.sort()
nums = 0
for d in spisok_1:
    if nums < len(d):
       nums = len(d)
       x = d
stroka_2 = ('Самое длинное название продукта {0} длинна {1} символов').format(x, len(x))
print(stroka_2)

