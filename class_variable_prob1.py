# class variable
# cicle 
# area 
# circumference
class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def calc_circumference(self):
        return 2 * Circle.pi * self.radius

    def calc_area(self):
        return Circle.pi * (self.radius ** 2)

c = Circle(4)
c1 = Circle(5)

print(c.calc_circumference())
print(c1.calc_circumference())

print(c.calc_area())
print(c1.calc_area())