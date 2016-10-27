# list for loop
listloop = [1,2,3]
for x in listloop:
    print(x)

# dict for loop
dictloop = {'sachin': 31, 'Sujata': 30, 'Aaradhya': 3}
print("\nLopping over a dictionary")
for x in dictloop:
    print(x)

# tuple for loop
tupleloop = ('test', '1', 'test4')
print("\nLooping over a Tuple")
for x in tupleloop:
    print(x)

# using ranges function
print("\nLopping over a range single argument")
for x in range(10):
    print(x)

print("\nLooping over a range two arguments")
for x in range(1, 10):
    print(x)

print("\nLopping over a range three arguments")
for x in range(1, 10, 2):
    print(x)

print("\nLooping over a range backwards")
for x in range(10, -1, -1):
    print(x)

# Enumerate function
print("\nEnumeration")
s = "hello"
for index, c in enumerate(s):
    print(index, c)

# Summing a comma-seperated string of integers
print("\nSumming a comma-seperated string of integers")
s = "1,2,3,4,5,6,7,8,9,10,100,1000"
total = 0
for x in s.split(','):
    total = total + int(x)
print(total)
