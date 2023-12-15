import random

names = input ("Please enter the names separted by comma... ")

names_split = names.split(",")

length_of_names = len(names_split)

random_payer = random.randint(0, length_of_names - 1)

print (f"{names_split[random_payer]} is going to pay the bill today. ")