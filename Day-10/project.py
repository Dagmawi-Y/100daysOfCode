import os
import art

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculate():
    print(art.logo)
    x = float(input("What is the first number? "))
    for operation in operations:
        print(operation)
        should_continue = True

    while should_continue:
        chosen_op = input("Pick an operation: ")
        y = float(input("What is the next number? "))
        calc_function = operations[chosen_op]
        answer = calc_function(x, y)
        print (f"{x} {chosen_op} {y} = {answer}")

        if (input(f"Type 'y' to keep calculating with {answer}, or type n to start a new calculation.")) == "y":
            x = answer
        else:
            should_continue = False
            os.system("cls")
            calculate()

calculate()