import random

def guess_the_number():
    print("Welcome, Hero!")
    print("Your evil villain Mr. Beast has hidden a secret number between 1 to 30.")
    print("You have 5 chances to crack the code and save the day!")
    print("Use your mind powers...")
    print("Suit up... Mission begins now!\n")

    secret_number = random.randint(1, 30)
    attempts = 0
    max_attempts = 5
    score = 0

    print("You must crack it in 5 rounds or Mr. Beast will know!")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: "))
            attempts += 1

            if guess == secret_number:
                print("You did it, Hero! The world is safe again!")
                score += 10
                break
            elif guess < secret_number:
                print("Too low, Hero! Reach higher!")
            else:
                print("Too high, Hero! Aim lower!")

        except ValueError:
            print("Please enter a number between 1 to 30, Hero!")

    else:
        print(f"Mission failed! Mr. Beast knew it... The number was {secret_number}.")

    print(f"Your score: {score}")
    print("Game over, Hero!")

# Call the function
guess_the_number()

