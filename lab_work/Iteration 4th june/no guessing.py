import random
# Generate a secret number between 1 and 50
secret_number = random.randint(1, 50)
attempts = 0
guess = 0
print("I'm thinking of a number between 1 and 50.")
# Loop until the correct number is found
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess > secret_number:
        print("Too High")
    elif guess < secret_number:
        print("Too Low")
    else:
        print("Correct Guess")
# Display the total number of attempts
print(f"It took you {attempts} attempts to find the secret number!")