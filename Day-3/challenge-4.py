# small 15
# mid 20
# large 25

# pep for small 2
# pep for mid and large 3

# extra cheese 1

print("Welcome to Python Pizza.")
size = input("Please enter the pizza size you want. S, M or L?  ")
peproni = input ("Do you want peproni to be added? type Y or N.  ")
extra = input ( "Do you want extra cheese to be added? Y or N.  " )

total_bill = 0

if size == "S":
    total_bill += 15
elif size == "M":
    total_bill += 20
elif size == "L":
    total_bill += 25
else:
    print("Please enter a valid size. ")

if peproni == "Y":
    if size == "S":
        total_bill += 2
    else:
        total_bill += 3

if extra == "Y":
    total_bill += 1

print(f"The total bill is: {total_bill}")