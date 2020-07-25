import random


def guessing_game():
    number = random.randint(0, 100)
    while True:
        guess = int(input("Guess a number: "))
        if guess > number:
            print(f"Too high")
        elif guess < number:
            print(f"Too low")
        else:
            print(f"Just right")
            break


if __name__ == "__main__":
    guessing_game()
