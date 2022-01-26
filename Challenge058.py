#----------* CHALLENGE 58 *----------
# Make a maths quiz that asks five questions by randomly generating two whole numbers to make the question
# (e.g. [num1] + [num2]). Ask the user to enter the answer. If they get it right add a point to their score. At 
# the end of the quiz, tell them how many they got correct out of five.

from itertools import count
import random

print("Welcome to the Math Quiz!")
print("-----------------------------")

score = 0
counter = 5

print("Start!")
while counter > 0:
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)

    print("How is",num1,"+",num2,"= ")
    answer = int(input())
    res = num1 + num2
    if answer == res:
        score = score + 1
    counter = counter - 1

if score == 5:
    print("Congratulations! You had a perfect score.")
elif score > 0 and score < 5:
    print("Great! Your score is",score)
else:
    print("Keep going! You need to study more.")