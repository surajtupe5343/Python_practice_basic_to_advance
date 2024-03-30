l1 = ['user1', 'user2', 'user3', 'user4']
names = ['suraj', 'harshit', 'mohit', 'rohit']
list2 = list(zip(l1,names))
l3 = zip(*list2)
print(list(l3))
print(list2)

n1 = [1, 5, 6, 9, 85, 2]
n2 = [2, 3, 7, 8, 55, 5]
n3 = [5, 10, 15, 20, 25, 30]
print(tuple(max(pair) for pair in zip(n1,n2)))
print(list(zip(n1,n2,n3)))
for i in ((zip(n1,n2,n3))):
    print(sum(i)/len(i))