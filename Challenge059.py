#----------* CHALLENGE 59 *----------
# Display five colours and ask the user to pick one. If they pick the same as the program has chosen, say “Well
# done”, otherwise display a witty answer which involves the correct colour, e.g. “I bet you are GREEN with envy”
# or “You are probably feeling BLUE right now”. Ask them to guess again; if they have still not got it right,
# keep giving them the same clue and ask the user to enter a colour until they guess it correctly.

import random
colors = ['green','red','blue','orange','pink']
colorRand = random.choice(colors)
guess = False

print("------ Color Quiz! ------")
print("Choose a color:\n1.Green\n2.Red\n3.Blue\n4.Orange\n5.Pink")
answer = input("\n")
while answer != colorRand:
    answer = str.lower(answer)
    if answer == colorRand:
        print("Well Done!")
    else:
        if colorRand == 'blue':
            print("You are probably feeling BLUE.")
        elif colorRand == 'green':
            print("It's time to be GREEN and help nature.")
        elif colorRand == 'red':
            print("Awww, your chicks are RED right now.")
        elif colorRand == 'orange':
            print("I think it's better if you finish your ORANGE juice.")
        elif colorRand == 'pink':
            print("You're seem to start being so amorous and PINK.")
        answer = input("Let's try again\n")

print("The color was",colorRand)