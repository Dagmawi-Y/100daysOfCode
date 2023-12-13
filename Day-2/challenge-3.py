age = input("What is your current age? ")

age_num = int(age)

days = age_num * 365.25

months = int(days / 30)

years = int(months / 12)

print(f"You have lived {years} years, {months} months & and {days} days.")