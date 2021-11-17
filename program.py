class Person:
    pass
class Circle:
    pass
p1 = Person()
c1 = Circle()

print('isinstance(p1, Person)', isinstance(p1, Person))
print('isinstance(c1, Person)', isinstance(c1, Person))
print('isinstance(c1, Circle)', isinstance(c1, Circle))
print('type(p1) == Person', type(p1) == Person)