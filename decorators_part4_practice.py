from functools import wraps
def print_function_data(function):
    @wraps(function)
    def wraper_func(*args, **kwargs):
        print(f"You are calling {function.__name__} function")
        print(function.__doc__)
        return function(*args, **kwargs)
    return wraper_func

@print_function_data
def add(a,b):
    """This function takes two numbers as argument and return their sum"""
    return a+b

print(add(4,5))

@print_function_data
def multiplication(a,b):
    """This function takes two numbers as argument and return their multiplication"""
    return a*b

print(multiplication(4,5))
