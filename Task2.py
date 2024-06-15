
import random

def hangman():
    list_of_words = ['eduyear', 'hangman', 'india', 'laptop', 'pencil', 'batman', 'spectrum', 'headphone']
    word = random.choice(list_of_words)
    turns = 10
    guessmade = ""
    valid_entry = set("abcdefghijklmnopqrstuvwxyz")

    while turns > 0:
        main_word = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main_word += letter
            else:
                main_word += "_ "

        if main_word.replace(" ", "") == word:
            print(main_word)
            print("You won!!!")
            break

        print("Guess the word:", main_word)
        guess = input()

        if guess in valid_entry and guess not in guessmade:
            guessmade += guess
        else:
            print("Enter a valid character or a character you haven't guessed yet")

        if guess not in word:
            turns -= 1
            print(f"{turns} turns left!!!")

            if turns == 9:
                print("------------")
            if turns == 8:
                print("------------")
                print("      O      ")
            if turns == 7:
                print("------------")
                print("      O      ")
                print("      |      ")
            if turns == 6:
                print("------------")
                print("      O      ")
                print("      |      ")
                print("     /       ")
            if turns == 5:
                print("------------")
                print("      O      ")
                print("      |      ")
                print("     / \\    ")
            if turns == 4:
                print("------------")
                print("     \\O     ")
                print("      |      ")
                print("     / \\    ")
            if turns == 3:
                print("------------")
                print("     \\O/    ")
                print("      |      ")
                print("     / \\    ")
            if turns == 2:
                print("------------")
                print("     \\O/|   ")
                print("      |      ")
                print("     / \\    ")
            if turns == 1:
                print("Only 1 turn left!!! Hangman on his last breath")
                print("------------")
                print("     \\O/_|  ")
                print("      |      ")
                print("     / \\    ")
            if turns == 0:
                print("You lose")
                print("You let a good man die")
                print("The word was:", word)

name = input("Enter your name: ")
print("Welcome", name, "!")
print("----------------------")
print("Try to guess the word in less than 10 attempts")
hangman()
