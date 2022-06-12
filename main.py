import random

possibleOption = ["R", "S", "P"]

# Multiline comment
print("""You want to play Rock, Paper and Scissors?
Please Note the following abbreviation:
""")
print("R - Rock")
print("S - scissors")
print("P - Paper")
print("")

# CPU
computer = random.choice(possibleOption)
if computer == "R":
    CPU = "Rock"
if computer == "P":
    CPU = "Paper"
if computer == "S":
    CPU = "Scissors"


# Player choice
user = None

while user not in possibleOption:
    user = input("Make your choice - R, P or S : ").upper()  # convert user entry to uppercase
    if user == "R":
        player = "Rock"
    if user == "P":
        player = "Paper"
    if user == "S":
        player = "Scissors"


while player == CPU:
    print("Player (", player, "): " "CPU (", CPU, ")")
    print("Tie! - You need to choose again")

    computer = random.choice(possibleOption)
    if computer == "R":
        CPU = "Rock"
    if computer == "P":
        CPU = "Paper"
    if computer == "S":
        CPU = "Scissors"

    user = None
    while user not in possibleOption:
        user = input("Make your choice - R, P or S : ").upper()  # convert user entry to uppercase
        if user == "R":
            player = "Rock"
        if user == "P":
            player = "Paper"
        if user == "S":
            player = "Scissors"


if user == 'R':
    if computer == 'S':
        print("Player (", player, "): " "CPU (", CPU, ")")
        print("You win!")

if user == 'R':
    if computer == "P":
        print("Player (", player, "): " "CPU (", CPU, ")")
        print("You lose!")

if user == 'S':
    if computer == 'R':
        print("Player (", player, "): " "CPU (", CPU, ")")
        print("You lose!")

if user == 'S':
    if computer == 'P':
        print("Player (", player, "): " "CPU (", CPU, ")")
        print("You win!")

elif user == 'P':
    if computer == 'S':
        print("Player (", player, "): " "CPU (", CPU, ")")
        print("You lose!")

if user == 'P':
    if computer == 'R':
        print("Player (", player, "): " "CPU (", CPU, ")")
        print("You win!")


#print("Player - ", user)
#print("CPU -", computer)
