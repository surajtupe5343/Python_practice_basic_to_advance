# Create a laptop class with attributes like brand name, model name, price
# Create two object/instance of your laptop class
class Laptop:
    def __init__(self, laptop_name, model, price): # (self, laptop_name, model, price) are attributes.
        # instance variables below
        self.laptop_name = laptop_name
        self.model = model
        self.price = price
        self.full_name = laptop_name + ' ' + model # you can create more instance variables than attributes
        self.descreption = laptop_name + ' ' + model + ' ' + str(price) # price is in "int" type

m1 = Laptop('Dell', 'Lattitude 1', 70000)
m2 = Laptop('Lenovo', 'Random 1', 55000)
m3 = Laptop('HP', 'Au114Tx', 75000)

print(m1.price)
print(m2.full_name)
print(m3.descreption)