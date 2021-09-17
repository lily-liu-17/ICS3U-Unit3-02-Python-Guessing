#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Sept 2021
# This lets user guess a number
# Program will say right or wrong

import canstant


def main():
    # This lets user guess a number

    # input
    guess_number = int(input("Enter a number between 1-9 : "))

    # process
    if guess_number == canstant.ANSWER:
        print("You guessed correctly!")
    if guess_number != canstant.ANSWER:
        print("You guessed wrong!")

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
