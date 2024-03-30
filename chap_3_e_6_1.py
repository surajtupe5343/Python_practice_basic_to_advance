# from typing import get_origin

import random
winning_number = random.randint(1,100)
guess = 1
number = int(input("Enter the number between 1 to 100: "))
game_over = False
while not game_over:
    if number== winning_number:
        print(f"You win and you guessed this number in {guess} times.")
        game_over = True
    else:
        if number < winning_number:
            print("Too low...")
            guess+=1
            # print(9-guess, "Chance left to guess")
            number = int(input("Guess Again!\n"))
        else:
            print("Too high...")
            guess+=1
            # print(9-guess, "Chance left to guess")
            number = int(input("Guess Again!\n"))
    