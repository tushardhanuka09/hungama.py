import random

# List of predefined words related to Computer Science
word_list = ["algorithm", "function", "variable", "compile", "iterate", 
             "recursion", "binary", "array", "syntax", "pointer"]

def select_word():
    """Selects a random word from the word list."""
    return random.choice(word_list)

def display_hangman_header(attempts):
    """Displays the 'HANGMAN' header with a pointer under it."""
    print("\nHANGMAN")
    print(" " * attempts + "^")

def play_game():
    """Runs a single game of Hangman."""
    word_to_guess = select_word()
    guessed_letters = set()
    correct_guesses = set()
    attempts = 0
    max_attempts = 7  # Length of "HANGMAN"

    print("Welcome to Hangman!")
    display_hangman_header(attempts)

    # Display the initial word state with underscores
    word_display = ["_" for _ in word_to_guess]
    print(" ".join(word_display))

    while attempts < max_attempts:
        guess = input("\nGuess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        # Check if letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.add(guess)

        # Check if guess is correct
        if guess in word_to_guess:
            print("Good guess!")
            correct_guesses.add(guess)
            # Reveal the correctly guessed letters in the word
            word_display = [letter if letter in correct_guesses else "_" for letter in word_to_guess]
            print(" ".join(word_display))

            # Check if the player has guessed the word
            if "_" not in word_display:
                print("Congratulations! You guessed the word:", word_to_guess)
                print("Phew... you are saved.")
                break
        else:
            print("Wrong guess!")
            attempts += 1
            display_hangman_header(attempts)
            print(" ".join(word_display))

    if attempts == max_attempts:
        print("You are hanged. The word was:", word_to_guess)

def main():
    """Main function to control game flow."""
    while True:
        play_game()
        replay = input("\nWould you like to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()

