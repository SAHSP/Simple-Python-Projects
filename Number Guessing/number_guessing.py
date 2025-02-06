# Print welcome message for the game
print("Welcome To Number Guessing Game!")

# Import the random module to generate random numbers
import random

# Define the function for guessing the number
def guess_number():
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    
    # Initialize the user's guess to -1 (a value that is guaranteed to be wrong initially)
    guess = -1
    
    # Set the number of chances the user has to guess correctly
    chance = 5
    
    # Start a loop that runs as long as the guess is not correct and chances remain
    while guess != number and chance != 0:
        # Ask the user to input a guess
        guess = int(input("Guess a number between 1 and 100: "))
        
        # Decrease the chance by 1 after each guess
        chance -= 1
        
        # Provide feedback if the guess is too low
        if guess < number:
            print("Too low!")
        
        # Provide feedback if the guess is too high
        elif guess > number:
            print("Too high!")
        
        # If the guess is correct, print a success message and exit the function
        else:
            print("You guessed it!")
            print(":) :) :) :) :)  *^* Congratulations *^*  :) :) :) :) :)")
            return  # End the function as the game is won
    
    # If the loop ends (i.e., chances are used up), print a failure message
    print("You failed to Guess")
    
    # Reveal the correct number to the user
    print("The number was: ", number)

# Call the guess_number function to start the game
guess_number()
