s = set('abc')
s.add('d')
print(s)

s = set('abc')
s.clear()
print(s)

x = set('abc')
y = x
z = x.copy()
x.add('d')
print(x)
print(y)
print(z)

y = set('abcdef')
x = set('defghi')
y.difference(x)
print(y.difference(x))



y = set('abcdef')
x = set('defghi')
y.difference_update(x)
print(y)

x = set('abcd')
x.discard('a')
print(x)

y = set('abcdef')
x = set('defghi')
print(y.intersection(x))

y = set('abc')
x = set('def')
print(y.isdisjoint(x))
y.add('d')
print(y.isdisjoint(x))

y = set('abc')
x = set('abc')
print(y.issubset(x))
y = set('ab')
print(y.issubset(x))
y.add('z')
print(y.issubset(x))

y = set('abc')
x = set('abc')
print(y.issuperset(x))
y.add('z')
print(y.issuperset(x))

x = set('abc')
print(x.pop())

x = set('abc')
x.remove('a')
print(x)

y = set('abcdef')
x = set('defghi')
print(y.symmetric_difference(x))

y = set('abcdef')
x = set('defghi')
print(y.union(x))

y = set('abcdef')
x = set('defghi')
y.update(x)
print(y)






