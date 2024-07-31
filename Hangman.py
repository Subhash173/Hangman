import random

def hangman():

    # List of words to guess
    words = ['python', 'developer', 'programming', 'hangman', 'computer']

    # Select a random word from the list
    word = random.choice(words)

    # Create a list to store the guessed word, initially with underscores
    guessed_word = ['_'] * len(word)

    # Set the number of attempts
    attempts = 6

    # List to store the letters that have been guessed
    guessed_letters = []

    print("Welcome to Hangman Game!")
    print("You have 6 attempts to guess the word.")
    print("The word is:", ' '.join(guessed_word))

    # Main game loop
    while attempts > 0:

        # Get a letter guess from the user
        guess = input("Guess a letter: ").lower()
        pass
        # Validate the input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter. Try another one.")
            continue

        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess in word:

            # Update the guessed word with the correct letter
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
            print("Good guess!")
        else:
            # Deduct an attempt for an incorrect guess
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        # Display the current progress of the guessed word
        print("Word:", ' '.join(guessed_word))

        # Check if the user has guessed the entire word
        if '_' not in guessed_word:
            print("Congratulations! You've guessed the word:", word)
            break
    else:
        # If the user runs out of attempts, display the correct word
        print("Sorry, you've run out of attempts. The word was:", word)

# Run the game
hangman()
