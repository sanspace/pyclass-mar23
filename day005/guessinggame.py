import random

n = random.randint(1, 10)

for _ in range(6):
    guess = int(input("Enter your guess (1-10):"))
    if guess > n:
        print("You guessed higher")
    elif guess < n:
        print("You guessed lower")
    else:
        print("You guessed correct!")
        exit()
