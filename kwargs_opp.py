# kwargs (keywords arguments)
# **kwargs (double star operator)

# kwrags as parameter
def func(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(f"{k} : {v}")

# dictionary unpacking
d = {'name':'Suraj', 'age':23}
func(first_name = 'Suraj', last_name = 'Tupe', age = 23)
func(**d)