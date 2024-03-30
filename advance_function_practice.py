# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = [7, 8, 9]
average = lambda l1, l2, l3: [int(sum(i)/len(i)) for i in zip(l1,l2,l3)]
print(average([7, 8, 9], [4, 5, 6], [1, 2, 3]))

# --------------Solution using *args method----------------

average2 = lambda *args: [sum(i)/len(i) for i in zip(*args)]
print(average2([7, 8, 9], [4, 5, 6], [1, 2, 3], [10, 11, 12], [13, 14, 15]))