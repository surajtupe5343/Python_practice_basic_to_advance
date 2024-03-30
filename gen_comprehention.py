# generators are iterators(they don't reapet)
# generator comprehention is same as listb comperhention 
# the only diffrence is we use parenthesis"()" instead of square bracket"[]"
square1 = (i**2 for i in range(1,11))
print(square1)

# print(next(square1))
# print(next(square1))
# print(next(square1))

for num in square1:
    print(num)

for num in square1:
    print(num)

