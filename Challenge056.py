#----------* CHALLENGE 56 *----------
# Randomly pick a whole number between 1 and 10. Ask the user to enter a number and 
# keep entering numbers until they enter the number that was randomly picked.

import random

numRandom = random.randint(1,10)
num = int(input("Enter a number: "))

while num != numRandom:
    num = int(input("Enter a number again: "))

print("Correct!")