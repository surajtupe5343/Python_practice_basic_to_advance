def sort_list(l):
    odd_list = []
    even_list = []
    for i in l:
        if i%2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return [odd_list,even_list]

l1 = 1,2,3,4,5,6,7,8,9
print(sort_list(l1))
