# while loop string
s = 'stop'

while s != "stop":
    s = input("Enter a string: ")
    print(s)
print("exiting")

# while loop number
a = 9

while a >= 10:
    print(a)
print("numeric loop")

# example: 2
x = -30
y = 30

while x <= y:
    print(x)
    x = x + 1
    while x <= 0:
        print("X has nagative value")
        x += 1

# while else
#Let’s say you want to write the first ten numbers as in example 1 above.
#But for the final number (i.e. 10), you want to write “The final count is: “.
count = 0
while count < 10:
    print("current count is:")
    print(count)
    count += 1
else:
    print("The final count is:")
    print(count)

# While Loops and Lists

# creating a list of names
names = ['John', 'Paul', 'George', 'Sachin', 'Kiran', 'Vinod']

# creating variable that will hold our count
i = 0

# creating while loop
while i < len(names): #len(names) is used to check lenght of names list
    print(names[i]) # print out names list
    i += 1 # Increases i so that subsequent iteams in the list can be printed

# complex while loop
#In this example, we’ll build our own list of countries we’ve traveled to.
#We’ll collect raw input from the user and use and if-statement to verify input,
#as can be seen in the code below:

# creating empty list
countries = []

# creating variable that will control number of countires we can possibly Enter
count = 0

# creating while loop
while count < 5: # This ensure that only five list of countires can be entered
    print("Please enter a country you have been to")
    next = input("==> ")
    # if condition to verify user input
    if len(next) > 0 and next.isalpha():
        countries.append(next)
        print(countries)
        count = count + 1
    else:
        print("I'm sorry, but I can not accept that inputs")
