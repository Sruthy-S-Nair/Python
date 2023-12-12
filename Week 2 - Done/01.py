import random
secretNumber = random.randint(1, 10)

while True:
    guess = int(input("Enter a number between 1 and 10: "))
    if guess == secretNumber:
        print("Congratulations! You guessed the number correctly!")
        break
    elif guess > secretNumber:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")