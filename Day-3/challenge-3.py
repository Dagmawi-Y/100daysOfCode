# number should be divisible by 4
# then the number should not be divisible by a 100
# then that same number should be divisible by 400

# if all the conditions are true, the number is a leap year. otherwise its not.

year = int(input("Please enter a year to know if its a leap or not. "))

if ( year % 4 == 0 ):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print ("The number is a leap year.")
        else:
            print ("The number is not a leap year.")
    else:
        print ("The number is a leap year.")
else:
    print ("The number is not a leap year.")