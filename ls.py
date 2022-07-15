name = input('Как тебя зовут \t')
age = input('Сколько тебе лет \t')
age = int(age)
if 70 > age > 16:
    print(f'Welcome {name} on our website')
elif age == 16:
    print(f'Dear {name} need to wait one year.')
elif 70 <= age <= 121:
    print(f'You are lucky {name} and welcome.')
elif age > 121:
    print(f'You are not real {name}.')
else:
    print(f"I'm sorry {name} you are too young.")




x = 15
y = 4

print('x + y =', x+y)
print('x - y =', x-y)
print('x * y =', x*y)
print('x / y =', x/y)
print('x // y =', x//y)
print('x ** y =', x**y)
print('x > y —', x>y)
print('x < y —', x<y)
print('x == y —', x==y)
print('x != y —', x!=y)
print('x >= y —', x>=y)
print('x <= y —', x<=y)

x = True
y = False

print('x and y —', x and y)
print('x or y —', x or y)
print('not x —', not x)



x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3]
y3 = [1, 2, 3]

print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)



x = 'Nitro Sense'
y = {1:'a', 2:'b'}

print('N' in x)
print('Acer' not in x)
print(1 in y)
print('б' in y)