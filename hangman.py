import random

words = ["python", "computer", "program", "coding", "software"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_attempts:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses)

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    print("Game Over!")
    print("The word was:", word)