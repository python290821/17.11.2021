
class Person:
    def __init__(self, id, name, age, height):
        self.id = id
        self.name = name
        self.age = age
        self.height = height

    def __lt__(self, other): # <
        # compare None...
        # check if both objects are persons ....
        if isinstance(other, Person) == False:
            # throw error
            return False
        #return self.id < other.id
        #return self.age < other.age
        #return self.height < other.height
        #return self.name < other.name
        if self.id == other.id:
            return self.name < other.name
        else:
            return self.id < other.id

    def __repr__(self):
        return f'\tPerson(id={self.id}, name={self.name}, age={self.age}, ' \
               f'height={self.height}\n';

l1 = [3, 6, -2, 3] # min: 3, 6 < 3
l1.sort()
print('sorted le', l1)
danny = Person(1, 'danny', 20, 1.7)
suzi_sister = Person(3, 'dana', 35, 1.8)
suzi = Person(3, 'suzi', 35, 1.8)
moshe = Person(2, 'moshe', 21, 1.87)
_list_person = [suzi, moshe, danny, suzi_sister] # min: suzi, moshe < suzi
_list_person.sort()
print(_list_person)

