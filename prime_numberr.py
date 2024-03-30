# num = int(input("Enter the number:\n"))

# for i in range(2,7):
#     if num == 3 or num == 5 or num == 7:
#         print("Prime Number...!")
#         break
#     elif num % i ==0:
#         print("Not Prime...!")
#         break
# else:
#     print("Prime Number...!")

# -------------------SOLUTION FOR PRINTING THE PRIME NUMBERS-----------------


lower = int(input("Enter the lower interval: "))
upper = int(input("Enter the upper interval: "))
for num in range(lower, upper+1):
    if num>1:
        for i in range(2, num):
            if (num%i) == 0:
                break
        else:    
            print(num)       

# --------------CODING NINJA SOLUTION FOR PRINTING THE PRIME NUMBERS-----------

# n = int(input())
# d = 2
# flag = False
# while d < n:
#     if (n % d == 0):
#         flag = True
#     d = d + 1

# if flag:
#     print("not prime")
# else:
#     print("prime")