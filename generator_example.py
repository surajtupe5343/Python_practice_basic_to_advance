# create your first generator with generator function   

def num(n):
    for i in range(1, n+1):
        yield(i)

print(num(10))

for numbers in num(10):
    print(numbers)