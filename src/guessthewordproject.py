import random

# List of words to guess
words = ['python', 'java', 'kotlin', 'javascript']
guessed_word = random.choice(words)
hint = guessed_word[0] + guessed_word[-1]
store_g_1 = []
max_attempts = 6  # Maximum number of attempts

# Welcome message
a = input("Enter your name: ")
print("Welcome", a, "to the game of Guess the Word!")
print("You have", max_attempts, "attempts to guess the word.")

# Game loop
for attempt in range(max_attempts):
    print(f"\nAttempt {attempt + 1} of {max_attempts}")
    letter = input("Enter a letter: ").lower()

    # Validate input
    if len(letter) != 1:
        print("Please enter a single letter.")
        continue

    # Check if the letter is in the word
    if letter in guessed_word:
        if letter not in store_g_1:
            print("Good guess!")
            store_g_1.append(letter)
        else:
            print("You already guessed that letter.")
    else:
        print("Oops! That letter is not in the word.")

    # Show guessed letters so far
    guessed_so_far = ''.join([letter if letter in store_g_1 else '_' for letter in guessed_word])
    print("Word so far:", guessed_so_far)

    # Check if the word is fully guessed
    if guessed_so_far == guessed_word:
        print("Congratulations! You guessed the word correctly.")
        break

    # Offer a hint
    clue_requested = input("Do you want a hint? (yes/no): ").lower()
    if clue_requested == 'yes':
        print("Hint: The first and last letters are", hint)

# Final guess
else:
    print("\nYou've used all your attempts!")
    word_guess = input("Guess the word: ").lower()
    if word_guess == guessed_word:
        print("Congratulations! You guessed the word correctly.")
    else:
        print("Sorry, that's not the correct word.")

# Reveal the word
print("The word was:", guessed_word)
input("Press Enter to exit.")