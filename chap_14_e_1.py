import time
from functools import wraps
def calculate_time(func1):
    @wraps(func1)
    def wrapper(*args, **kwargs):
        print(f"Executing {func1.__name__} function.")
        t1 = time.time()
        returned_value = func1(*args, **kwargs)
        t2 = time.time()
        total_time = t2 - t1
        print(f"This function took {total_time} seconds")
        return returned_value
    return wrapper

@calculate_time
def square_finder(n):
    return [i**2 for i in range(1, n+1)]

square_finder(5000)
print(square_finder(10))