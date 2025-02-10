import random

# Function to read words from a file
def read_words_from_file(filename):
    with open(filename, 'r') as file:
        # Read lines and strip any leading/trailing whitespace
        words = [line.strip() for line in file]
    return words

# Function to scramble a word
def scramble_word(word):
    scrambled = ''.join(random.sample(word, len(word)))
    return scrambled

# Main game function
def play_scramble_game():
    # Read words from 'words.txt'
    words_list = read_words_from_file('words.txt')
    
    score = 0
    rounds = 5  # Number of rounds
    
    print("Welcome to the Word Scramble Game!")
    
    for _ in range(rounds):
        # Choose a random word and scramble it
        word = random.choice(words_list)
        scrambled = scramble_word(word)
        
        print(f"\nScrambled word: {scrambled}")
        
        # Get the user's guess
        guess = input("Guess the word: ").lower()
        
        if guess == word:
            print("Correct! +1 point.")
            score += 1
        else:
            print(f"Wrong! The correct word was: {word}")
    
    # Show the final score
    print(f"\nGame over! Your final score is: {score}/{rounds}")

# Start the game
play_scramble_game()
