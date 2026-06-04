secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the Number: "))
    
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
    else:
        print("Wrong Guess. Try Again.\n")