def evans(n):
    for i in range(1, n+1):
        if i%2 == 0:
            yield(i)

evans_generator = evans(7)

for i in evans_generator:
    print(i)

for i in evans_generator:
    print(i)
# this will print only once because of generator