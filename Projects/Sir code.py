import pywhatkit as wa
from phone numbers import *
import time

# Create a list of contacts
individuals = [vinod, sso1, sso2, lyla, sai_perso, hr_phone, dinesh_da]
groups = [hn_admin]

# Create a message
message1 = '''
Subject: Clock-in reminder for 24 June 2023 🕒

Dear team💕,

This is a friendly reminder to always make sure you are properly clocking in every morning as soon as you enter HERE AND NOW. Staying on top of your time cards is important for accuracy when it comes to measuring your work ethics. 🙌

Please contact HR immediately if you have technical issues.📞

Have a nice work day!😊
Caramel AI🍬
'''
message2 = '''
Subject: Clock-in reminder nº3 🕒

Dear team💕,

This is a friendly reminder to always make sure you are properly clocking in every morning as soon as you enter HERE AND NOW. Staying on top of your time cards is important for accuracy when it comes to measuring your work ethics. 🙌

Please contact HR immediately if you have technical issues.📞

Have a nice work day!😊
Caramel AI🍬
'''
message3 = '''
Subject: Clock-in reminder nº4 🕒

Dear team💕,

This is a friendly reminder to always make sure you are properly clocking in every morning as soon as you enter HERE AND NOW. Staying on top of your time cards is important for accuracy when it comes to measuring your work ethics. 🙌

Please contact HR immediately if you have technical issues.📞

Have a nice work day!😊
Caramel AI🍬
'''

# Send the message to individuals
for individual in individuals:
    wa.sendwhatmsg_instantly(individual, message1, 15, True, 3)

# Send the message to groups
for group in groups:
    wa.sendwhatmsg_to_group_instantly(group, message1, 15, True, 3)

print("Reminder Nº1 Sent Successfully")

time.sleep(7200)

# Send the message to individuals
for individual in individuals:
    wa.sendwhatmsg_instantly(individual, message2, 15, True, 3)

# Send the message to groups
for group in groups:
    wa.sendwhatmsg_to_group_instantly(group, message2, 15, True, 3)

print("Reminder Nº2 Sent Successfully")

time.sleep(7200)

# Send the message to individuals
for individual in individuals:
    wa.sendwhatmsg_instantly(individual, message3, 15, True, 3)

# Send the message to groups
for group in groups:
    wa.sendwhatmsg_to_group_instantly(group, message3, 15, True, 3)

print("Reminder Nº3 Sent Successfully")