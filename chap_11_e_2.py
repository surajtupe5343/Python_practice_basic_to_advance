# function
# list, reverse_str = True
# list

def func(*args, **kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in args]
    else:
        return [name.title() for name in args]

names = ['harshit', 'mohit', 'suraj']
print(func(*names, reverse_str = True))