
n = int(input())
m = int(input())
row = 1

while row <= n:
    col = 1
    while col <= m:
        print(row * col, end=" ")
        col += 1
    print()
    row += 1

# ------------------SOLUTION USING FOR LOOP-----------------

n = int(input())
m = int(input())
row = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        print(i * j, end=" ")
    print()

# for num in range(1, rows):

#     for i in range(num):

#         print(num, end=" ") # print number

#     print()