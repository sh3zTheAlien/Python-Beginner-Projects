import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

print(art.logo)

x = 1
while x == 1:
    first_number = float(input("What's the first number? "))
    condition = True
    while condition:
        operator = input("+\n-\n*\n/\nPick an operation: ")
        second_number = float(input("What's the next number? "))

        answer = operations[operator](first_number, second_number)

        print(f"{first_number} {operator} {second_number} = {answer}")

        continue_calculation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if continue_calculation == "y":
            first_number = answer
        else:
            condition = False