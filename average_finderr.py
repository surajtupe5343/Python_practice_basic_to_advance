def average1(*args):
    average = []
    for pair in zip(*args):#--> here *args use for unpack lists in one tuple for eg.([1,2,3],[4,5,6],[7,8,9])
        average.append(sum(pair)/len(pair))#---> we use just (args) for loop in common list or tuple
    return average

print(average1([1,2,3],[4,5,6],[7,8,9]))

#---------------SAME SOLUTION IN ONE LINE---------------

average2 = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]
print(average2([1,2,3],[4,5,6],[7,8,9]))