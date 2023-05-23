from random import randint


def get_random_number():
    return randint(1,21)

def get_guess():
    return input("Enter your guess")

tries = 5
answer = get_random_number()
for _ in range(tries):
    guess = get_guess()
    if guess == answer:
        print("Right")
        exit()
    if guess > answer:
        print("Higher guess")
    if guess < answer:
        print("Lower guess")


def fun_name(args):
    ...
    return return_value
