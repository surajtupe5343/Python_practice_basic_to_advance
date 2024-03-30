def merge_list(l,m):
    one_list = []
    for i in l:
        if i in m:
            one_list.append(i)
    return one_list

l1 = [1,2,5,6]
l2 = [1,2,7,8]
print(merge_list(l1,l2))    