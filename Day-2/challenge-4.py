
num = float(input ("What was the total bill? "))

while True:
    try:
        tip = float(input("What percentage of tip would you like to give? 10, 12 or 15? "))
        if tip in [10, 12, 15]:
            break
        else:
            print("please enter a percentage value in 10, 12 or 15")
    except:
        ValueError("Please enter a valid number.")

num_of_people = int(input("How many people will split the bill? "))

tip_decimal = tip / 100

splitted_tip = round((num + (tip * tip_decimal)) / num_of_people, 2)

print(f"Each person should pay: {splitted_tip}")