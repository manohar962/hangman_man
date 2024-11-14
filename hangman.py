import random

# List of words for the game
word_list = ["algorithm", "function", "variable", "compile", "iterate", "recursion", "binary", "array", "syntax", "pointer"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(word_list)

# Function to display the current state of the guessed word
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

# Function to play the game
def hangman():
    word = choose_word()  # Select a random word
    guessed_letters = []  # Store letters that have been guessed
    incorrect_guesses = 0  # Track the number of incorrect guesses
    max_incorrect_guesses = 6  # Set the maximum number of incorrect guesses allowed

    print("Welcome to Hangman!")
    print("Try to guess the word. You have a maximum of 6 incorrect guesses.")

    while incorrect_guesses < max_incorrect_guesses:
        print("\nCurrent word: ", display_word(word, guessed_letters))
        
        guess = input("Enter a letter: ").lower()

        # Check if the input is a valid single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue

        # If the letter has already been guessed
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Oops! '{guess}' is not in the word.")

        # Check if the player has guessed all letters
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}\nPhew.. you are saved")
            break
    else:
        print(f"\nSorry, you've run out of attempts. The word was: {word}\nYou are hanged")

if __name__ == "__main__":
    hangman()

