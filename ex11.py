from random import randint

high_num = 50
low_num = 0
number_to_guess = randint(low_num,high_num)
number_guessed = -9999999

while number_to_guess != number_guessed:
    number_guessed = int(input(f"Guess a number between {low_num} and {high_num}: "))

    if number_guessed == number_to_guess:
        print(f"Well done! The number was {number_to_guess}")
    elif number_guessed > number_to_guess:
        print("Your number is higher than the number you need to guess")
    else:
        print("Your number is lower than the number you need to guess")
