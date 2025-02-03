import random

def coin_toss_game():
    print("Welcome to the Coin Toss Game!")
    print("You can guess either 'heads' or 'tails'.")
    
    score = 0
    rounds = 5  # Let's play 5 rounds for this example
    
    for _ in range(rounds):
        player_guess = input("Guess heads or tails: ").lower()
        
        # Check for valid input
        if player_guess not in ["heads", "tails"]:
            print("Invalid guess! Please enter 'heads' or 'tails'.")
            continue
        
        # Simulate a coin toss (random choice between heads and tails)
        coin_result = random.choice(["heads", "tails"])
        print(f"The coin landed on: {coin_result}")
        
        # Check if player's guess matches the result
        if player_guess == coin_result:
            print("You guessed it right! +1 point")
            score += 1
        else:
            print("Sorry, you guessed wrong.")
        
        print(f"Your current score: {score}")
        print()
    
    print(f"Game over! Your final score: {score} out of {rounds}")

# Run the game
coin_toss_game()
