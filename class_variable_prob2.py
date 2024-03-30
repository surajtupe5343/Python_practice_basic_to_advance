class Laptop:
    discount_percent = 10
    def __init__(self, laptop_name, model, price): # (self, laptop_name, model, price) are attributes.
        self.laptop_name = laptop_name
        self.model = model
        self.price = price
        self.full_name = laptop_name + ' ' + model # you can create more instance variables than attributes
        self.descreption = laptop_name + ' ' + model + ' ' + str(price) # price is in "int" type
    
    def apply_discount(self):
        return self.price - ((self.price * self.discount_percent)/100)


m1 = Laptop('Dell', 'Lattitude 1', 100000)
m2 = Laptop('Lenovo', 'Random 1', 55000)
m3 = Laptop('HP', 'Au114Tx', 63000)

m2.discount_percent = 50
print(m2.__dict__)
print(m2.apply_discount())


print(m1.apply_discount())
print(m3.apply_discount())