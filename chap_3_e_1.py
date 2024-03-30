import random
# n = random.randint(0,10)
n = 5
gs = int(input("Guess the number: "))
if n>gs:
    print("Too Low")
elif n<gs:
    print("Too High")
else:
    print("You WoN!!")
    