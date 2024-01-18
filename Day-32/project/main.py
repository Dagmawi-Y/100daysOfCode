import datetime as dt
import random
import pandas
import smtplib

my_email = "daggyohannes@gmail.com"
my_password = "qauxllxfpeerieoz"

# ---------- Extra Hard Starting Project ------------
now = dt.datetime.now()
today = (now.month, now.day)
print(today)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(birthday_dict)

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    letter_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(letter_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
