import random 

dice_roll = {
    1 : ("┌─────────┐",
         "│         │",
         "│    ●    │",
         "│         │",
         "└─────────┘"),
    2 : ("┌─────────┐",
         "│  ●      │",
         "│         │",
         "│       ● │",
         "└─────────┘"),
    3 : ("┌─────────┐",
         "│  ●      │",
         "│    ●    │",
         "│      ●  │",
         "└─────────┘"),
    4 : ("┌─────────┐",
         "│  ●   ●  │",
         "│         │",
         "│  ●   ●  │",
         "└─────────┘"),
    5 : ("┌─────────┐",
         "│  ●   ●  │",
         "│    ●    │",
         "│  ●   ●  │",
         "└─────────┘"),
    6 : ("┌─────────┐",
         "│  ●   ●  │",
         "│  ●   ●  │",
         "│  ●   ●  │",
         "└─────────┘")
}


dice= []
total = 0 
num = int(input("How many dice do want to roll : "))

for roll in range(num):
    dice.append(random.randint(1,6))

for roll in range(num):
    for line in dice_roll.get(dice[roll]):
        print(line) 

for roll in dice:
    total += roll 

print(f"Total number = {total}")


