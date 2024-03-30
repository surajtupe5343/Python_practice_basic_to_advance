class Person:
    def __init__(self, first_name, last_name, age):
        # instance variables
        print('init method(constroctor) fet called')
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person(last_name='Suraj', first_name='Tupe', age=23)
p2 = Person('Sanket', 'Tupe', 26)

print(p1.first_name)
print(p2.first_name)