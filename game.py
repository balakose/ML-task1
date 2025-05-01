# guessing game
import random
secret_number=random.randint(1,100)

for i in range(5):
    guess=input("enter your guess:")
    if not guess.isdigit():
        print("invalid input. try again.")
        continue
    guess=int(guess)
    if guess==secret_number:
        print("you guessed it right")
        break
    else:
        print("wrong guess.")
        print("game over.")








