#----------* CHALLENGE 54 *----------
# Randomly choose either heads or tails (“h” or “t”). Ask the user to make their choice. If their choice is the same
# as the randomly selected value, display the message “You win”, otherwise display “Bad luck”. At the end, tell
# the user if the computer selected heads or tails.

import random
from re import I
coin = ["h","t"]

answer = input("Heads or Tails? [h|t]")

azar = random.choice(coin)
answer = str.lower(answer)

if answer == azar:
    print("You win!")
else:
    print("Bad luck")

print("Your choose was "+answer+" and the coin was "+azar)