import smtplib
import datetime as dt
import random
import pandas

#
my_email = "daggyohannes@gmail.com"
my_password = "qauxllxfpeerieoz"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="linkdaggy@gmail.com",
#         msg="Subject: Hello\n\nHello from python."
#     )


# date_time = dt.datetime
# now = date_time.now()
#
# date_of_birth = dt.datetime(year= 1995, month= 12, day= 15,)
# print(date_of_birth)

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 3:
    with open("quotes.txt", "r") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Monday Motivation\n\n{quote}",

        )
