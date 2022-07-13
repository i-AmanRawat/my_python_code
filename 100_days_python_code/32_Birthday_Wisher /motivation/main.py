import smtplib
import datetime as dt
import random

my_mail = "yourmail@gmail.com"
my_password = "yourpassword"
now = dt.datetime.now()
day_of_week = now.weekday()     #tells day in number

if day_of_week == 0:        #0 -->  monday
    with open("quotes.txt") as quote_file :     #openning the quote file
        list_of_quotes = quote_file.readlines()     #converting the quote file into a list
        quote = random.choice(list_of_quotes)       #picking up a random quote out from the list
    print(quote)

    with smtplib.SMTP("outlook.office365.com") as connection :  #connecting with the server of the gamil
        connection.starttls()       #tls -> transport layer security
        connection.login( user = my_mail , password = my_password )     #logging in
        connection.sendmail(
            from_addr= my_mail,
            to_addrs= my_mail,
            msg= f"Subject: Monday \n\n {quote}"
        )

'''
    my program is not working reason being: gmail has stopped giving access to the third party # security -> less secure app access has been turned off by google permanently
'''


# import smtplib  #simple mail transfer protocol library
#
# my_mail = "day32temporary@outlook.com"
# password = "day32fortrailpurpose"
#
# with smtplib.SMTP("outlook.office365.com") as connection:
#     connection.starttls()       #transport layer security
#     connection.login(user = my_mail , password = password)
#     connection.sendmail(
#         from_addr = my_mail ,
#         to_addrs = "coders.entrepreneur.2021@gmail.com" ,
#         msg = "Subject: Testing things out \n\n mail through python 's smtplib"
#     )

#
# import datetime as dt
#
# now = dt.datetime.now()
# day = now.day
# year = now.year
# month = now.month
# time = now.time()
# day_of_week = now.weekday()
# print(day_of_week)
#
# DOB = dt.datetime(day= 15, month=5, year=2020)
# print(DOB)