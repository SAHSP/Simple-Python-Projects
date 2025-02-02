# Print welcome message for the game
print("Let's Play Rock, Paper, and Scissors Game!")

# Import the random module for generating random choices for the computer
import random

# Instructions for the user
print("You can type rock, paper, or scissors")
print("5 points to win")

# Initialize counters for computer and user scores
c1 = 0  # Computer's score
c2 = 0  # User's score

# Dictionary to map choices to numbers for easier comparison
d = {"rock": 1, "paper": 2, "scissors": 3}

# Start a loop that runs until either player or computer reaches 5 points
while c1 != 5 and c2 != 5:
    # Ask the user to input their choice
    x = input("Enter your choice: ")
    
    # Convert the user's choice to lowercase to handle case-insensitive input
    x = x.lower()
    
    # Check if the user's input is valid (i.e., one of the keys in the dictionary)
    if x not in list(d.keys()):
        # If invalid input, show error message and restart the loop
        print("   **** WRONG ENTRY ****")
    else:
        # Convert the user's choice to its corresponding number (rock=1, paper=2, scissors=3)
        x = d[x]
        
        # Generate a random choice for the computer (1=rock, 2=paper, 3=scissors)
        y = random.randint(1, 3)
        
        # Check if it's a tie
        if x == y:
            print("It's a tie")
        
        # Check if the user wins based on the game rules
        elif (x == 1 and y == 3) or (x == 2 and y == 1) or (x == 3 and y == 2):
            print("Point to You   +1  :)")
            c2 += 1  # Increment user's score
        
        # If none of the above conditions are met, the computer wins the round
        else:
            print("Point lost :( ")
            c1 += 1  # Increment computer's score
        
        # Print the current score after each round
        print()
        print(f"Score Yours: {c2} and Computer: {c1}")

# When either the user or computer reaches 5 points, check who won
if c1 == 5:
    print("You Lost ")
    print("TRY AGAIN")
else:
    print("You Won")
