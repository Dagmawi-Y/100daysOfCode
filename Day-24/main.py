#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
letter_new = ""
with open("Input/Names/invited_names.txt", "r") as names_from_file:
    names = (names_from_file.read().split())
    print(names)

for name in names:
    with open("Input/Letters/starting_letter.txt", "r") as letter:
        letter_read = letter.read()
        letter_new = letter_read.replace("[name]", f"{name}")
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(letter_new)




#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp