import time

# t1 = time.time()
# l = [i**2 for i in range(1000000)]
# print(time.time()- t1)

# for i in l:
#     print(i)

t1 = time.time()
g = (i**2 for i in range(1000000))
print(time.time()- t1)

# for i in g:
#     print(i)