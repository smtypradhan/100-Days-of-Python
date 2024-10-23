import random

#word_list pulled from hangman_words.py
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6 

# display logo from hangman_art.py and print at start of the game
print(logo)

# Randomly choose a word from the word_list and assigned to variable chosen_word
chosen_word = random.choice(word_list)

#placeholder with same number of blanks as the chosen_word
placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"

print(placeholder)

#While loop 
game_over = False
correct_letters = []

while not game_over:
    #variable guess in lowercase
    print(f"**************You have {lives} lives left.**************")
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in correct_letters:
        print(f"You've already guessed {guess}. Try again.")

    #display variable for putting the guessed letter in the right position  
    display = ""

    #for loop to keep the previous correct letters in display
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess) 
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print("*************You Lose. Game Over!**************")

    if "_" not in display:
        game_over = True
        print("**************You Win. Game over!**************")

    print(stages[lives])