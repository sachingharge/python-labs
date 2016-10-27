#
# Example file for working with timedelta objects
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print (timedelta(days=365, hours=5, minutes=1))

# print today's date
print ("Today is:  " + str(datetime.now()))

# print today's date one year from now
print ("one year from now it will be: " + str(datetime.now() + timedelta(days=365)))

# create timedelta that uses more than one arguments
print ("in two weeks and 3 days it will be: " + str(datetime.now() + timedelta(weeks=2, days=3)))

# calculate the date 1 week ago, formatted as a string
time = datetime.now() - timedelta(weeks=1)
s = time.strftime("%A %B %d, %Y")
print ("one week ago it was " + s)

### How many days until Sachin's Brithday?

today = date.today() # get the today's date
sachin_birthday = date(today.year, 4, 3) # get the Brithday for same year
# use date comparison to see if birthday has already gone for this year
if sachin_birthday < today:
    print ("Sachin Birthday already went by %d days ago" % ((today - sachin_birthday).days))
    sachin_birthday = sachin_birthday.replace(year=today.year + 1) # if so, get the day for next year

# Now calculate the amount of time until next birthday
time_to_sachin_birthday = abs(sachin_birthday - today)
print (time_to_sachin_birthday.days, "days until next Sachin's Birthday")

### How many days until Aaradhya's Brithday?
aaradhya_birthday = date(today.year, 2, 28) # get the Brithday for same year
# use date comparison to see if birthday has already gone for this year
if aaradhya_birthday < today:
    print ("Aaradhya Birthday already went by %d days ago" % ((today - aaradhya_birthday).days))
    aaradhya_birthday = aaradhya_birthday.replace(year=today.year + 1) # if so, get the day for next year

# Now calculate the amount of time until next birthday
time_to_aaradhya_birthday = abs(aaradhya_birthday - today)
print (time_to_aaradhya_birthday.days, "days until next Aaradhya's Birthday")
