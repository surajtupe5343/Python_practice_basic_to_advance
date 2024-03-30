class Laptop:
    def __init__(self, laptop_name, model, price): # (self, laptop_name, model, price) are attributes.
        # instance variables below
        self.laptop_name = laptop_name
        self.model = model
        self.price = price
        self.full_name = laptop_name + ' ' + model # you can create more instance variables than attributes
        self.descreption = laptop_name + ' ' + model + ' ' + str(price) # price is in "int" type
    
    def apply_discount(self, discount_in_percentage):
        return self.price - ((self.price * discount_in_percentage)/100)


m1 = Laptop('Dell', 'Lattitude 1', 100000)
m2 = Laptop('Lenovo', 'Random 1', 55000)
m3 = Laptop('HP', 'Au114Tx', 63000)

print(m1.apply_discount(40))
print(m3.apply_discount(10))