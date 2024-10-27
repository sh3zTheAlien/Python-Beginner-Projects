import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

final_list = []


for random_letters in range(nr_letters):
    x = (random.choice(letters))
    final_list.append(str(x))

for random_symbols in range(nr_symbols):
    y = (random.choice(symbols))
    final_list.append(str(y))

for random_numbers in range(nr_numbers):
    c = random.choice(numbers)
    final_list.append(str(c))

random.shuffle(final_list)
combine_final = "".join(final_list)
print(f"Your password is: {combine_final}")





