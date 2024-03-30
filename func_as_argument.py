def square(a):
    return a**2

l = [1, 2, 3, 4]
# print(list(map(lambda a : a**2, l)))

def my_map(func, l1):
    new_list = []
    for item in l1:
        new_list.append(func(item))
    return new_list

def my_map2(func, l2):
    return [func(i) for i in l2]

print(my_map(square, l)) 
print(my_map(lambda a: a**3, l))
print(my_map2(lambda a: a**3, l))