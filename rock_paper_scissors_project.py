import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Mine solution
computer_choose = random.randint(0, 2)
user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if user_input == "0":
    print(rock,"Computer chose:")

    if computer_choose == 0:
        print(rock)
        print("It's a draw.")
    elif computer_choose == 1:
        print(paper)
        print("You lose")
    else:
        print(scissors)
        print("You win!")

elif user_input == "1":
    print(paper, "Computer chose:")

    if computer_choose == 0:
        print(rock)
        print("You win!")
    elif computer_choose == 1:
        print(paper)
        print("It's a draw")
    else:
        print(scissors)
        print("You lose")

elif user_input == "2":
    print(scissors, "Computer chose:")

    if computer_choose == 0:
        print(rock)
        print("You lost")
    elif computer_choose == 1:
        print(paper)
        print("You Win!")
    else:
        print(scissors)
        print("It's a draw")

else:
    print("You entered wrong input rerun the program.")


