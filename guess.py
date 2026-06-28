import random

target = random.randint(1, 100)
guess = int(input("Guess the number (1-100): "))

attempts = 1

while guess != target:
    if guess < target:
        print("Too low! Guess higher.")
    elif guess > target:
        print("Too High! Guess Lower.")
    guess = int(input("Guess again (1-100): "))
    attempts += 1

print(f"Correct! You got it in {attempts} guesses!")
