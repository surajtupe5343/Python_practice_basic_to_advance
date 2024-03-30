# def greater_smaller(a,b):
#     if a > b:
#         return f"{a} is greater than {b}"
#     elif a == b:
#         return f"{a} is equal to {b}"
#     return f"{a} is smaller than {b}" 
    
# a = float(input("Enter first nuber: "))
# b = float(input("Enter second nuber: "))
# print(greater_smaller(a,b))

# ---------------SOLUTION[2]--------------

# def greater(a,b):
#     if a > b:
#         return a
#     else:
#         return b

# num1 = int(input ("enter first number ")) 
# num2 = int(input("enter second number ")) 
# bigger = greater (num1, num2,)

# print (f" {bigger} is greater")

# ---------------SOLUTION[3]--------------

def greatest(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b    
    else: #c > a and c > b:
        return c

num1 = int(input ("enter first number ")) 
num2 = int(input("enter second number ")) 
num3 = int(input("enter third number ")) 
bigger = greatest(num1, num2, num3)

print(f" {bigger} is greater")

# ---------------SOLUTION[4]--------------

# def new_greatest(a,b,c):
#     bigger = greater(a,b)
#     return greater(bigger, c)
# print(f"{bigger} is greater")    