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

small = 15
medium = 20
large = 25

pep_s = 2
pep_m_l = 3

extra_cheese = 1

total_bill = 0


if (size == "S"):
    total_bill = small
if (size == "S" and peproni == "Y"):
    total_bill = small + pep_s
if (size == "S" and peproni == "Y" and extra == "Y"):
    total_bill = small + pep_s + extra_cheese

if (size == "M"):
    total_bill = medium
if (size == "M" and peproni == "Y"):
    total_bill = medium + pep_m_l
if (size == "S" and peproni == "Y" and extra == "Y"):
    total_bill = medium + pep_m_l + extra_cheese

if (size == "L"):
    total_bill = large
if (size == "L" and peproni == "Y"):
    total_bill = large + pep_m_l
if (size == "L" and peproni == "Y" and extra == "Y"):
    total_bill = large + pep_m_l + extra_cheese

print(f"The total bill is: {total_bill}")