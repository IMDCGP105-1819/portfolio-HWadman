# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"
vowels = ['a','e','i','o','u']

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    letters_in_both = 0
    secret_word_guessed = "".join(get_guessed_word(secret_word, letters_guessed))

    if secret_word_guessed == secret_word:
        return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    guessed_word = []

    for i in secret_word:
        if i in letters_guessed:
            guessed_word.extend(str(i))
        else:
            guessed_word.extend("_")

    return guessed_word

def get_available_letters(letters_guessed):
    available_letters = []

    for i in string.ascii_lowercase:
        available_letters.extend(str(i))

    for i in letters_guessed:
        if i in available_letters:
            available_letters.remove(i)

    return available_letters

def is_valid_letter(letter_to_check):
    for i in string.ascii_lowercase:
        if letter_to_check == i:
            return True
    return False

def is_vowel(letter_to_check):
    for i in vowels:
        if letter_to_check == i:
            return True
    return False

def hangman(secret_word):
    guesses_left = 6
    letters_guessed = []
    correct_input = False
    warnings = 3
    end = False
    total_score = 0

    print(f"The word to guess contains {len(secret_word)} letters. You have {guesses_left} guesses.")

    while is_word_guessed(secret_word,letters_guessed) == False:

        if guesses_left < 1:
            print(f"You used up all your guesses. The answer was \"{secret_word}\".")
            return

        correct_input = False
        print(f"You have {guesses_left} guesses left.")
        print("You have not yet guessed the letters", "".join(get_available_letters(letters_guessed)))

        while correct_input == False:
            letter_last_guessed = str(input("Please input the singular letter you wish to guess: "))
            letter_last_guessed = letter_last_guessed.lower()

            if len(letter_last_guessed) != 1 or is_valid_letter(letter_last_guessed) == False:
                warnings -= 1
                print(f"Please input only 1 letter from the alphabet. You have {warnings} warnings left!")
                correct_input = False
            else:
                correct_input = True

            for i in letters_guessed:
                if i == letter_last_guessed:
                    warnings -= 1
                    print(f"That letter has already been guessed. You have {warnings} warnings left!")
                    correct_input = False

            if warnings < 1:
                warnings = 3
                guesses_left -= 1
                print(f"You have been warned 3 times, you now have {guesses_left} guesses left.")
                if guesses_left < 1:
                    print(f"You used up all your guesses. The answer was \"{secret_word}\".")
                    end = True
                    return

        if end:
            return

        pre_guessed_word = get_guessed_word(secret_word, letters_guessed)
        letters_guessed.extend(letter_last_guessed)
        post_guessed_word = get_guessed_word(secret_word, letters_guessed)

        print("")

        if post_guessed_word == pre_guessed_word:
            print(f"{letter_last_guessed} is not in the word.")
            if is_vowel(letter_last_guessed):
                guesses_left -= 1
                print("The letter you guessed was a vowel so you lose 2 guesses")
            else:
                print("The letter you guessed was a consonant so you lose 1 guess")
        else:
            print(f"{letter_last_guessed} is in the word.")
            guesses_left += 1

        print("--------------------------------------------")
        print(get_guessed_word(secret_word, letters_guessed))
        print("--------------------------------------------")

        print("")

        if is_word_guessed(secret_word, letters_guessed):
            print("Well done you guessed the word!")
            total_score = (guesses_left - 1) * (len("".join(set(secret_word))))
            print(f"You scored {total_score}")

        guesses_left -= 1

secret_word = choose_word(wordlist)
hangman(secret_word)
