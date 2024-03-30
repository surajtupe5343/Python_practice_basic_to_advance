s = input("Enter the numbuer containing two or more digits:\n")
i = 0
total = 0
while i < len(s):
    total += int(s[i])
    i+=1
print("Total of your all digits are:",total)
