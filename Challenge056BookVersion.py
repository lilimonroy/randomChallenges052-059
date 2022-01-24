#----------* CHALLENGE 56 BOOK *----------
# Randomly pick a whole number between 1 and 10. Ask the user to enter a number and 
# keep entering numbers until they enter the number that was randomly picked.

import random
num = random.randint(1,10)
correct = False
while correct == False:
    guess = int(input("Enter a number: "))
    if guess == num:
        correct = True