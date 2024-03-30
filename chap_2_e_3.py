name, ch1 = input("Enter your full name and one char seprated by ',' : ").split(",")
print("Length of your name is\n",len(name.strip()))#-->it will print length with spaces
# a = name.lower() or name.upper()
print(f"Character count is {name.strip().lower().count(ch1.strip().lower())}")
# In above method if user gives extra spaces between two inputs then count function will return 0 
#so we can remove spaces using .strip function for example-->
# name.strip()# .lstrip will remove left side spaces so the .rstrip will righht side
# ch1.strip()#-->and .strip function will remove both side spaces.
# print(a.count(ch1))
#you can remove all(between two words) spaces by using replace method 
# for example
print(name.replace(" " , ""))