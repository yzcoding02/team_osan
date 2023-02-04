import random

def hangman():
    # List of words to choose from
    word_list = ["JASMIN"]
    word = random.choice(word_list)
    word = word.upper()
    word_letters = set(word)
    alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    used_letters = set()
    word_guessed = set()
    tries = 6
    print("Welcome to Hangman!\n")
    print("You have", tries, "tries to guess the word.")
    print(" ".join(list("_" * len(word))))
    while (len(word_letters) > 0) and (tries > 0):
        print("You have used the following letters:", " ".join(used_letters))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                word_guessed.add(user_letter)
                print(" ".join(list(letter if letter in word_guessed else "_" for letter in word)))
            else:
                tries -= 1
                print("Incorrect.")
                print("You have", tries, "tries left.")
        elif user_letter in used_letters:
            print("You have already used this letter.")
        else:
            print("Invalid Input")
    if tries > 0:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Sorry, you did not guess the word. The word was", word)

hangman()
