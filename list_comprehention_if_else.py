#---------------Normal Solution for if-else List Creating-----------------

l1 = list(range(1,11))
l2 = []
for i in l1:
    if i%2 == 0:
        l2.append(i*2)
    else:
        l2.append(-i)
print(l2)

#---------------Solution for if-else List Creating using List Comprehention-----------------

l3 = [i*2 if i%2 == 0 else -i for i in range(1,11)]
print(l3)