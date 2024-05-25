import random

def get_random_word():
    # A small list of 5-letter words
    words = ["apple", "grape", "peach", "berry", "lemon", "mango", "melon", "plumb", "guava"]
    return random.choice(words)

def display_feedback(guess, secret):
    feedback = []
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            feedback.append('🟩')  # Green for correct position
        elif guess[i] in secret:
            feedback.append('🟨')  # Yellow for wrong position
        else:
            feedback.append('⬜')  # Gray for not in the word
    return ''.join(feedback)

def wordle():
    secret_word = get_random_word()
    attempts = 6
    print("Welcome to Wordle! Guess the 5-letter word.")

    for attempt in range(attempts):
        guess = input(f"Attempt {attempt + 1}/{attempts}: ").lower()

        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue

        feedback = display_feedback(guess, secret_word)
        print(feedback)

        if guess == secret_word:
            print("Congratulations! You've guessed the word correctly.")
            break
    else:
        print(f"Sorry, you've used all attempts. The word was: {secret_word}")

# Run the game
wordle()
