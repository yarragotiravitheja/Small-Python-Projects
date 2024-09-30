# cook your dish here
import random

MAX_GUESSES = 10
NUM_DIGITS = 3


def bagel_game():
    while True:
        secretion = get_secretion()
        print("I have thought up a number")
        print("You have {} guesses to get it.".format(MAX_GUESSES))
        num_guesses = 1

        while num_guesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS and not guess.isdecimal():
                print("Guess #{}".format(num_guesses))
                guess = input('> ')

            clues = get_clues(guess, secretion)
            print(clues)
            num_guesses += 1

            if guess == secretion:
                break
            if num_guesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print("THe Answer was {}.".format(secretion))

        print("Do you want to play again? (yes or no)")
        if not input('> ').lower().startswith('y'):
            break

    print("Thanks for playing")


def get_secretion():
    numbers = list("1234567890")
    random.shuffle(numbers)

    secretion = ''
    for i in range(NUM_DIGITS):
        secretion += str(numbers[i])

    return secretion


def get_clues(guess, secretion):
    if guess == secretion:
        return "You got it!"

    clues = []

    for i in range(NUM_DIGITS):
        if secretion[i] == guess[i]:
            clues.append("Fermi")
        elif secretion[i] in guess:
            clues.append("Pico")
    if len(clues) == 0:
        clues.append("Bagels")
    return " ".join(clues)


def main():
    introduction = """
    Bagels, a deductive logic game,
    By Ravi Theja
    
    I am thinking of a 3-digit number, Try to a guess what it is.
    Here are some clues:
    when I say:         That means:
        Pico            One digit is correct but in the wrong position.
        Fermi           One digit is correct and in the right position.
        Bagels          No digit is correct.
    """
    print(introduction)
    bagel_game()


if __name__ == "__main__":
    main()
