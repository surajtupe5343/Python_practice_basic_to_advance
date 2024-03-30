def square_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square
n1 = int(input("Enter lower Interval: "))
n2 = int(input("Enter upper Interval: "))
list1 = list(range(n1,n2+1))
print(square_list(list1))