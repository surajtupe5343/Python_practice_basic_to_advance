# class method as a constructor
class Person:
    count_instance = 0 #--> Class Variable / Class Attribute
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,int(age))

    @classmethod
    def count_intances(cls):
        return f"You have created {cls.count_instance} instances of {cls.__name__} class."
    def full_name(self):  # self is important to write in every function in class. 
        return f'{self.first_name} {self.last_name}'

    def is_above_18(self):
        return self.age>18

p1 = Person('Suraj', 'Tupe', 23)
p2 = Person('Sanket', 'Tupe', 26)
p3 = Person.from_string('Harshit,Vashista,24')
print(p3.full_name())
print(p3.is_above_18())