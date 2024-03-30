#------------Normal Solution----------------

l1 = list(range(1,11))
l2 = []
for i in l1:
    if i%2==0:
        l2.append(i)

print(l2)

#------------Solution using List Cmprehention----------------

even1 = [i for i in l1 if i%2 == 0]
print(even1)
even2 = [i for i in range(1,11) if i%2 == 0]
print(even2)
odd1 = [i for i in range(1,11) if i%2 != 0]
print(odd1)
#------------Normal Solution using Function----------------

def even_list(l):
    list2 = []
    for j in l:
        if j%2 == 0:
            list2.append(j)
    return list2

print(even_list(list(range(1,11))))