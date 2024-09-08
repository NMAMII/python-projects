from hangmanbank import words,pics,logo
import random

print(logo)
chances = 6

chosen_word = random.choice(words)
guessed_letters = []

game_on = True
while game_on:
    print(f"Your chances = {chances}")
    player_guess = input("guess a letter: ").lower()
    word = ""
    if player_guess in guessed_letters:
        print(f"\nYou've already guessed the letter ({player_guess})\nChose another one.\n")

    for letter in chosen_word:
        if letter == player_guess:
            word += letter
            guessed_letters.append(player_guess)
        elif letter in guessed_letters:
            word += letter
        else:
            word += "_"

    if player_guess not in chosen_word:
        chances -= 1
        print(f"You guessed the letter ({player_guess}) wrong \n-1 chance ")
        print(pics[chances])
        if chances == 1:
            print(f"You guessed the letter ({player_guess}) wrong. \nBe careful you only have one chance left!  ")
            print(pics[chances])
    print(word)
    if "_" not in word:
        print("You win!")
        game_on = False
    elif chances == 0:
        print(f"\nYou lost!\nThe word was '{chosen_word}'.")
        game_on = False
