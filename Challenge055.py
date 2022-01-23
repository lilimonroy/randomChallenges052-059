##----------* CHALLENGE 55 *----------
# Randomly choose a number between 1 and 5. Ask the user to pick a number. If they guess correctly, display the message “Well done”,
# otherwise tell them if they are too high or too low and ask them to pick a second number. If they guess correctly on their second guess, display
# “Correct”, otherwise display “You lose”.
import random

numRand = random.randint(1,5)
count = 1

num = int(input("Enter a number between 1 and 5: "))
while count > 0:
    if num == numRand:
        print("Well done!")
        break
    elif num != numRand:
        if num > numRand:
            print("Too high!")
            count = count -1
            num = int(input(" Your last chance! Enter a number between 1 and 5: "))
        elif num < numRand:
            print("Too low!")
            count = count -1
            num = int(input(" Your last chance! Enter a number between 1 and 5: "))
        else:
            print("Error 2")
    else:
        print("Error 1")
if count == 0 and num != numRand:
    print("You loose. The number was",numRand)
else:
    print("Correct!")