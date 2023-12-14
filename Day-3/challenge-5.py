name1 = input("What is your name?  ").lower()
name2 = input("What is their name? ").lower()

true_count = 0
love_count = 0

combined_name = name1 + name2
true_count += combined_name.count("t")
true_count += combined_name.count("r")
true_count += combined_name.count("u")
true_count += combined_name.count("e")

love_count += combined_name.count("l")
love_count += combined_name.count("o")
love_count += combined_name.count("v")
love_count += combined_name.count("e")


love_score = int((f"{true_count}{love_count}"))

if (love_score < 10 or love_score > 90):
    print(f"Your love score is {love_score}: and you go together like Coke and Mentos. ")
elif (love_score > 40 and love_score < 50):
    print(f"Your love score is {love_score}: you are alright together. ")
else:
    print(f"Your love score is {love_score}. ")