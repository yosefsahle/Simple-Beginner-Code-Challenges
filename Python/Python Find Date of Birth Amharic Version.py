import time
import calendar
# Enter date in this format -> 19990606
# i.e. Year-month-day
# That is 1999 - Year, 06 - month, 06 - day
print("input Your date of birth like 19911202")
dt = input('')
a = (dt[0:4])
b = (dt[4:6])
c = (dt[6:8])
print('Your Date of Birth is:')
print(c + '-' + b + '-' + a)
x = str(a) + "-" + str(b) + "-" + str(c)
y = time.strftime("%A", time.strptime(x, "%Y-%m-%d"))
if y == "Monday":
    y = "ሰኞ"

if y == "Tuesday":
    y = "ማክሰኞ"

if y == "Wedensday":
    y = "ዕረቡ"

if y == "Thursday":
    y = "ሐሙስ"

if y == "Friday":
    y = "አርብ"

if y == "Saturday":
    y == "ቅዳሜ"

else:
    y == "እሁድ"

print('=====የተወለዱበት ቀን ' + y + ' ነበር=====')
