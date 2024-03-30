# FOR "while loop" eg. if input is 10--> o\p will be 1+2+3+....+10
total = 0
i = 1
j = int(input("Enter the number:\n"))
while i<=j:
    total+= i
    i+=1
print(total)
# FOR "for loop eg. input is 1234--> 1+2+3+4"

# j = int(input("Enter the number:\n"))
# total = 0 
# for i in range(1, j+1):
#     total+=int(i)
# print(total)