class Person:
    count_instance = 0 #--> Class Variable / Class Attribute
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    @classmethod
    def count_intances(cls):
        return f"You have created {cls.count_instance} instances of {cls.__name__} class."
    def full_name(self):  # self is important to write in every function in class. 
        return f'{self.first_name} {self.last_name}'

    def is_above_18(self):
        return self.age>18

p1 = Person('Suraj', 'Tupe', 23)
p2 = Person('Sanket', 'Tupe', 26)
print(Person.count_intances())