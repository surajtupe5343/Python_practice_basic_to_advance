import random
winning_number = random.randint(1,100)
guess = 1
while True:
    number = int(input("Enter the number between 1 to 100: "))
    if number== winning_number:
        print(f"You win and you guessed this number in {guess} times.")
        game_over = True
        break
    else:
        if number < winning_number:
            print("Too low...")
        else:
            print("Too high...")
            
        guess+=1
        continue
    