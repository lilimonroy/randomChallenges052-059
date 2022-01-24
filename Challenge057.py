#----------* CHALLENGE 57 *----------
# Update program 056 so that it tells the user if they are too high or too low before they pick again.

import random

numRandom = random.randint(1,10)
guess = False

while guess == False:
    num = int(input("Enter a number: "))
    if num == numRandom:
        print("Correct!")
        guess = True
    elif num > numRandom:
        print("To high.")
    elif num < numRandom:
        print("To low.")

print("The number was",numRandom)