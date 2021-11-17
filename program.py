import shelve

class Person:
    def __init__(self, id, name, age, height):
        self.id = id
        self.name = name
        self.age = age
        self.height = height

#danny = Person(id= 1, name='danny', age=20, height=1.89)
#s = shelve.open('people.db')
#s['1'] = danny.__dict__
#s['2'] = 'hello'
#s['3'] = 42
#  key  value
# '1':  {'id': 1, 'name': 'danny', 'age': 20, 'height': 1.89}
# '2':  'hello'
# '3':  42
s = shelve.open('people.db')
d = Person(1, None, 0, 0)
# long way ----------------
d.id = s['1']['id']
d.name = s['1']['name']
d.age = s['1']['age']
d.height = s['1']['height']
# short way ----------------
d.__dict__ = s['1']
print(d.__dict__)
s.close()
