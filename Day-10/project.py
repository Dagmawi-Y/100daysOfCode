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

x = int(input("What is the first number? "))

for operation in operations:
    print(operation)

chosen_op = input("Choose an operation from the list above: ")

y = int(input("What is the second number? "))

calc_function = operations[chosen_op]

answer = calc_function(x, y)

print (f"{x} {chosen_op} {y} = {answer}")