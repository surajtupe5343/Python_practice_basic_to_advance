from functools import wraps
def only_datatypes_allows(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if all([type(arg)== data_type for arg in args]):
                return function(*args, **kwargs)
            return "Invalid Argument."
        return wrapper
    return decorator

@only_datatypes_allows(str)
def string_join(*args):
    string = ''
    for i in args:
        string += i
    return string

print(string_join('suraj.','D.','tupe'))
print(string_join('suraj.','D.','tupe', 5))

@only_datatypes_allows(int)
def add_total(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add_total(1,2,3,4,5,))
print(add_total(1,2,3,4,5,6,7,[1,2,3]))
