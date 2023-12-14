print ("Welcome to the treasure island, your mission is to find the treasure.")

step1 = input("You\'re at a cross road, where do you want to go? left or right?").lower()
if(step1 == "left"):
    print ("You lost on your first step")
else:
    step2 = input("swim or wait?").lower()
    if(step2 == "swim"):
        print ("Game over on step 2.")
    else:
        step3 = input("which door?, red, blue or yellow?").lower()
        if(step3 == "red" or step3 == "blue"):
            print("Game over on step 3.")
        else:
            print("You Won!!!!")