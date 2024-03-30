# def palindrome(a):
#     if a[::-1] == a:
#         return True
#     return False    
# a = input("Enter the name:\n")
# print(palindrome(a))

# ---------------SOLUTION[2]---------------

def is_palindrome(a):
    return a == a[::-1]
a = input("Enter the name:\n")
print(is_palindrome(a))

# a = 'namann'
# b = a[-1::-1]
# print(b)