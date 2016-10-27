#
# Example file for working with Calendars
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

import calendar

#calendar.setfirstweekday(calendar.SUNDAY)

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2016, 10, 0, 0)
print (str)
print ("=========================")


c_local = calendar.LocaleTextCalendar(firstweekday='SUNDAY',locale='fr_FR')
locale_str = c.prmonth(2016, 10)
print (locale_str)
print ("=========================")

# create a HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2016, 10)
print (str)

print ("=========================")


# loop over days of the month
# zeroes mean that day of the week is an overlapping month
for i in c.itermonthdays(2016, 10):
    print (i)

print ("=========================")


# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
    print(name)
print ("=========================")

for abbr in calendar.month_abbr:
    print (abbr)
print ("=========================")

for day in calendar.day_name:
    print (day)
print ("=========================")

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
for m in range(1,13):
  # return array ofr weeks that reprsent the month
  cal = calendar.monthcalendar(2016, m)
  print (cal)
  # the first Friday has be within the first two weeks
  weekone = cal[0]
  weektwo = cal[1]

  # conditon
  if weekone[calendar.FRIDAY] != 0:
      meetday = weekone[calendar.FRIDAY]
  else:
  # if the first friday isn't in the first week, it must be in the second
    meetday = weektwo[calendar.FRIDAY]

    #print ("%10s %2d" % (calendar.month_name[m], meetday))
  print "%10s %2d" % (calendar.month_name[m], meetday)
