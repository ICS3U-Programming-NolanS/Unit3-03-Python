#!/usr/bin/env python3

# Created by: Nolan Shami
# Created on: October 21st, 2022
# This program asks the user to guess a number
# and tells them if they got it right.


import random


def main():

    guessed_number = int(input("Enter your number between 0 and 9: "))
    print("")

    random_variable = random.randint(1, 9)

    if guessed_number == random_variable:
        print("You guessed correctly!")

    else:
        print("You guessed incorrectly! The correct answer is: " + str(random_variable))


if __name__ == "__main__":
    main()
