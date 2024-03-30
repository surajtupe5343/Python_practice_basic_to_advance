from functools import wraps
def only_int_allows(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if all([type(arg)==int for arg in args]):
            return function(*args, **kwargs)
        return "Invalid Argument."
        # data_types = []
        # for arg in args:
        #     data_types.append(type(arg)==int)
        # if all(data_types):
        #     return function(*args, **kwargs)
        # return "Invalid Argument."
    return wrapper

@only_int_allows
def add_total(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add_total(1,2,3,4,5,))
print(add_total(1,2,3,4,5,6,7,[1,2,3]))