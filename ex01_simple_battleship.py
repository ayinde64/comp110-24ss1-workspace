"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730480705"

# Define emoji characters for boxes
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# Prompt Player 1 for their secret boat location
boat_location = input("Pick a secret boat location between 1 and 4: ")

# Convert the input to an integer
boat_location_int = int(boat_location)

# Check if the input from Player 1 is valid
if boat_location_int < 1:
    print("Error! Too low! Please pick a number between 1 and 4.")
    exit()  # Exit the program if input is invalid
elif boat_location_int > 4:
    print("Error! Too High! Please pick a number between 1 and 4.")
    exit()  # Exit the program if input is invalid
else:
    # If the input is valid, exit without printing anything
    pass

# Prompt Player 2 for their guess
guess = input("Guess a number between 1 and 4: ")

# Convert the input to an integer
guess_int = int(guess)

# Check if the input from Player 2 is valid
if guess_int < 1:
    print("Error! Too low! Please guess a number between 1 and 4.")
    exit()  # Exit the program if input is invalid
elif guess_int > 4:
    print("Error! Too high! Please guess a number between 1 and 4.")
    exit()  # Exit the program if input is invalid
else:
    # If the input is valid, exit without printing anything
    pass

# Check if Player 2's guess matches Player 1's boat location
if guess_int == boat_location_int:
    result = "\U0001F7E5"
else:
    result = "\U00002B1C"

# Initialize emoji string of boxes
emoji_boxes = ""

# Construct emoji string of boxes
for i in range(1, 5):
    if i == guess_int:
        emoji_boxes += result + " "
    else:
        emoji_boxes += "\U0001F7E6" + " "

# Print the resulting emoji string of boxes
print(emoji_boxes)
