#
# Example file for formatting time and date output
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined control codes
  now = datetime.now() # get the current date and time

  ### Date Formating ###

  # %y/%Y - Year, %a/%A - weekday, %b/%B - Month, %d - day of the month
  print (now.strftime("%Y")) # full year with century
  print (now.strftime("%A %d, %B, %Y"))

  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print (now.strftime("%c"))
  print (now.strftime("%x"))
  print (now.strftime("%X"))

  # time formating #####
  # %I/%H - 12/24 hour, %M - minute, %S - second, %p - locale's AM/PM
  print (now.strftime("%I:%M:%S %p")) # 12-Hour:Minute:Second:AM
  print (now.strftime("%H:%M")) # 24-Hour:Minute

if __name__ == "__main__":
  main();
