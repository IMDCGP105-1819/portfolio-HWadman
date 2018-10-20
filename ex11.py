from random import randint

high_num = 50
low_num = 0
number_to_guess = randint(low_num,high_num)
number_guessed = -9999999
number_of_guesses = 0

while number_to_guess != number_guessed:
    number_guessed = int(input(f"Guess a number between {low_num} and {high_num}: "))
    number_of_guesses += 1

    if number_guessed == number_to_guess:
        print(f"Well done! The number was {number_to_guess} it took you {number_of_guesses} guesses to reach that number")
    elif number_guessed > number_to_guess:
        print("Your number is higher than the number you need to guess")
    else:
        print("Your number is lower than the number you need to guess")
