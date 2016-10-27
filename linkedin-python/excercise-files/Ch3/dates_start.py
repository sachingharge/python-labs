#
# Example file for working with date information
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

from datetime import date
from datetime import time
from datetime import datetime


def main():
  ## DATE objects
  # Get today's date from simple today() method from date class
  today = date.today()
  print ("Today's date is ", today)

  # print date's individual components
  print ("Date Components: ", today.day, today.month, today.year)

  # retrive today's weekday (0=Monday, 6=Sunday)
  print ("Today's weekday #: ", today.weekday())

  ## DATETIME OBJECTS
  # Get today's date from datetime class
  today1 = datetime.now()
  print ("The current date and time is ", today1)

  # Get current time
  time = datetime.time(datetime.now())
  print ("The current time is ", time)

  # weekday returns 0 (monday) through 6 (sunday)
  wd = date.weekday(today)
  # Days start at 0 for Monday
  days = ["monday", "tuesday", "wednesday", "thursday", "Friday", "Saturday", "Sunday"]
  print ("Today is day number %d" %wd)
  print ("Which is a " + days[wd])

if __name__ == "__main__":
  main();
