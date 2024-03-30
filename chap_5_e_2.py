def reverse_list(l):
    list3 = []
    for i in range(len(l)):
        list1 = l.pop()
        list3.append(list1)
    return list3

list2 = [1 , 2, 3, 4, 5]
print(reverse_list(list2))
# print(list2[-1::-1])