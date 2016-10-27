#
# Example file for working with functions
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

# define a function
def func1():
    print ("I am a function")

func1()

print(func1())
print(func1)

# define a fuction that takes arguments
def func2(arg1, arg2):
    print (arg1, "Test", arg2)

func2(10,20)
print(func2(10,30))


# define a fuction with default value for argument
def power(num, x=1):
    result = 1;
    for i in range(x):
        result = result * num
    return result

print (power(2))
print (power(2,3))
print (power(x=3, num=2))


# function return a value
def cube(x):
    return x * x * x

print (cube(4))

# function with variable number of arguments
def multi_add(*args):
    result = 1;
    for x in args:
        result = result + x
    return result

print (multi_add(4,5,10,5))

id_test = id(func1())
print (id_test)
