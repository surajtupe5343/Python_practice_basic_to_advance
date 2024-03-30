from functools import wraps
def decorator_func(any_func):
    @wraps(any_func)
    def wraped_func(*args, **kwargs):
        """This is wrapper function"""
        print("This is awesome function..!")
        return any_func(*args, **kwargs)
    return wraped_func

@decorator_func
def add(a, b):
    """This is add function"""
    return a + b

# print(add(5, 2))

print(add.__doc__)
print(add.__name__)

# without using modules this will give output as following
# This is wrapper function
# wraped_func
