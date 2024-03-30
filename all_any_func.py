# "all" and "any" functions
n1 = [2, 4, 6, 8, 10]
n2 = [1, 5, 7, 8, 11]
print(all(i%2 == 0 for i in n1))
print(any(i%2 == 0 for i in n2))

# advance use of "all" and "any" function

def all_total(*args):
    #(1,2,3,4,5)
    if all([type(i)== int or type(i)== float for i in args]):
        total = 0
        for num in args:
            total += num
        return total
    else:
        return "Wrong Input....!"
t = all_total(1,2,3,4,5,)
t1 = all_total(1,2,3,4,5, 'suraj',[1,'sk'])
print(t) 
print(t1)