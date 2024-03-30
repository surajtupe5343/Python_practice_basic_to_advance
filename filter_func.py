# filter function
#  we use filter function to filter the list and convet into 
# list or tuple by using defined function(def) or lambda function

def is_even(a): 
    """This function returns all even numbers which are divisible by 2."""
    return a%2 ==0

numbers = [3, 4, 2, 1, 5, 6, 9, 8, 18]
evens = tuple(filter(is_even, numbers)) 
print(is_even.__doc__)
print(evens)

# ----------------SAME SOLUTION USING LAMBDA EXPRESSION-----------------

even2 = tuple(filter(lambda a: a%2 ==0, numbers)) 
print(even2)