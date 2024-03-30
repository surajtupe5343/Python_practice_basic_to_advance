# make flexible function

# *operators
# *args

# def total(a,b):
#     return a+b

def all_total(*args):
    #(1,2,3,4,5)
    total = 0
    for num in args:
        total += num
    return total
t = all_total(1,2,3,4,5)
print(t) 

def all_multyply(*args):
    #(1,2,3,4,5)
    multiply = 1
    for num in args:
        multiply *= num
    return multiply
m = all_multyply(1,2,3,4,5)
num = [5,6,7]
print(all_multyply(*num)) #use *num just like *args in function for unpack values in list or tuples.
print(m) 