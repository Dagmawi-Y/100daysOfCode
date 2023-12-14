print ("Welcome to the roller coaster!")
height = int(input("What is your height in cm?"))

if height > 120:
    age = int(input("How old are you? "))
    if age <= 12:
        print("You have to pay $5.")
    elif (age > 12 and age < 18):
        print("You have to pay $7.")
    else:
        print("You have to pay $12. ")
else:
     print("You are not allowed to use the rollercosater. ")
    

