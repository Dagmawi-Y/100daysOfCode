print ("Welcome to the roller coaster!")
height = int(input("What is your height in cm?"))
price = 0
total = 0

if height > 120:
    age = int(input("How old are you? "))
    if age <= 12:
        print("Child tickets are $5.")
        price = 5
    elif (age < 18):
        print("Youth tickets are $7.")
        price = 7
    elif (age >= 45 and age<= 55):
        print("Everything is going to be ok. have a free ride.")
    else:
        print("Adult tickets are $12. ")
        price = 12

    photo = input("Do you want a photo? y or n")
    if photo == "y":
        photo_price = 3
        total = price + photo_price
        print (f"You will pay a total of {total}")
    else:
        print (f"You will pay {price}")
    
else:
     print("You are not allowed to use the rollercosater. ")
    

