#---------------Solution using List Comprehention with Function-----------------

def changed_list(l):
    # new_list = []
    return [str(i) for i in l if  (type(i) == int or type(i)== float)]

list1 = [1, 2, 2.5, 3.5, 'suraj', [1, 2, 'li'], True, False, (5, 10, 15.5)]
print(changed_list(list1))

#---------------Solution using Function withot List Comprehention-----------------

def changed_list2(k):
    new_list = []
    for i in k:
        if  (type(i) == int or type(i) == float):
            new_list.append(str(i))
    return new_list

list2 = [1, 2, 2.5, 3.5, 'suraj', [1, 2, 'li'], True, False,
 (5, 10, 15.5), {'f':'press f', 's': 'start'}]
print(changed_list2(list2))