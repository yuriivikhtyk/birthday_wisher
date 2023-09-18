import pandas as pd
import random
import smtplib
import datetime as dt


# 1. Update the birthdays.csv
birthdays_data = pd.read_csv("birthdays.csv")
birthdays_dict = birthdays_data.to_dict(orient='records')
#print(birthdays_dict)


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day = now.day
month = now.month
#print(day, month)


send_email = False
name = ''
email = ''
for dict in birthdays_dict:
    if dict['day'] == day and dict['month'] == month:
        send_email = True
        name = dict['name']
        email = dict['email']

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
with open("letter_templates/letter_1.txt") as file:
    file1 = file.readlines()
with open("letter_templates/letter_2.txt") as file:
    file2 = file.readlines()
with open("letter_templates/letter_3.txt") as file:
    file3 = file.readlines()

birthday_wishes = [file1, file2, file3]
birthday_text = random.choice(birthday_wishes)
birthday_text = ''.join(birthday_text)
birthday_text = birthday_text.replace("[NAME]", name)
#print(birthday_text)


# 4. Send the letter generated in step 3 to that person's email address.
my_email = "your_email@gmail.com"
my_password = "app_password"


if send_email:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=email, 
            msg=f"Subject:Happy Birthday!\n\n{birthday_text}"
            )
else:
    print("No birthdays today.")


