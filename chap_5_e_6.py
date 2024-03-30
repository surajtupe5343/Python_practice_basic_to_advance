def sublist_counter(l):
    count = 0 
    for i in l:
        if type(i) == list:
            count+=1
    return count
mixed = [1,2,3,[56,8,84],[24,5,4,2],[4,2,1],5,8,4]
print(f"Number of lists present in list is {sublist_counter(mixed)}")