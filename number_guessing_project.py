import random
import art
print(art.logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

difficulty_choose = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

computer_guess = random.randint(1,100)

def hard_level():
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    while attempts != 1 and user_guess != computer_guess:
            if user_guess > computer_guess:
                attempts -= 1
                print(f"Too high\nGuess again.\nYou have {attempts} attempts remaining to guess the number.")
                user_guess = int(input(f"Make a guess: "))
            elif user_guess < computer_guess:
                attempts -= 1
                print(f"Too low\nGuess again.\nYou have {attempts} attempts remaining to guess the number.")
                user_guess = int(input(f"Make a guess: "))
    else:
        if attempts == 1 and user_guess != computer_guess:
            print("You've run out of guesses, you lose.")
        elif user_guess == computer_guess:
            print(f"You got it, the right answer was {computer_guess}")

def easy_level():
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    while attempts != 1 and user_guess != computer_guess:
        if user_guess > computer_guess:
            attempts -= 1
            print(f"Too high\nGuess again.\nYou have {attempts} attempts remaining to guess the number.")
            user_guess = int(input(f"Make a guess: "))
        elif user_guess < computer_guess:
            attempts -= 1
            print(f"Too low\nGuess again.\nYou have {attempts} attempts remaining to guess the number.")
            user_guess = int(input(f"Make a guess: "))
    else:
        if attempts == 1 and user_guess != computer_guess:
            print("You've run out of guesses, you lose.")
        elif user_guess == computer_guess:
            print(f"You got it, the right answer was {computer_guess}")

if difficulty_choose == "easy":
    easy_level()
elif difficulty_choose == "hard":
    hard_level()
else:
    print("You typed wrong inputs, rerun the program...")