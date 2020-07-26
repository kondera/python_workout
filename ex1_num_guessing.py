import random


def guessing_game():
    """
    Takes a number and prints if it's too high or low
    5 chances for guessing
    """
    chances = 5
    number = random.randint(0, 100)
    while chances > 0:

        try:
            guess = int(input("Guess a number: "))
        except ValueError:
            print("Try writing a number")
            continue

        if guess > number:
            print(f"Your guess: {guess} is too high")
            chances -= 1

        elif guess < number:
            print(f"Your guess: {guess} is too low")
            chances -= 1

        else:
            print(f"Just right")
            break

    if chances == 0:
        print("Well, you lose")


if __name__ == "__main__":
    guessing_game()
