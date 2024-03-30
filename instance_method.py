# instance methods
class Person:
    def __init__(self, first_name, last_name, age):
        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):  # self is important to write in every function in class. 
        return f'{self.first_name} {self.last_name}'

    def is_above_18(self):
        return self.age>18

p1 = Person('Suraj', 'Tupe', 23)
p2 = Person('Sanket', 'Tupe', 26)

print(p1.full_name())
print(p2.is_above_18())
# print(Person.full_name(p1)) # print(p1.full_name()) is working like this line in python

l = [1, 2, 3]
# clear, pop
# l.pop(1)
# l.clear()
# list.clear(l)
# l.append(10)# can also write like this list.append(l, 10)
list.append(l, 10)
print(l)