#5. Create a Number Guessing Game where:
#● The program generates a random number between 1 and 50 using random.
#● The user has 5 attempts to guess the number.

import random
import math

secret = random.randint(1,50)
attempts = 5
won = False

print("Number Guessing game ! Guess a number between 1 and 50:")
print("You have attempts", attempts, "attempts.")

for attempt in range(1, attempts+1):
    guess = int(input("Attempt" + str(attempt)+ "-Enter your guess:"))
    
    difference = math.fabs(secret - guess)

    if guess == secret:
        print("correct! you guessed the number in", attempt,"attempts.")
        won = True
        break
    else:
        print("wrong! your guess is",int(difference),"away from the correct number.")

if not won:
    print("Game over! the correct number was", secret)
