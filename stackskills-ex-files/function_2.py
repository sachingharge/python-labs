# function part-2

def add(a,b,c):
    print(a,b,c)
    return a + b +c

test = add(1,5,10)
print (test)
print ("----------------")

# pass arguments using *
args = (1,2,3)
test1 = add(*args)
print (test1)
print ("----------------")

# pass arguments using **
args1 = {'c' : 11, 'b' : 20, 'a' : 11}
dict_test = add(**args1)
print (dict_test)
print ("----------------")

# Using aribitrary argument list
def add_test(*numbers):
    print (numbers)
    return sum(numbers)

num_list1 = add_test(1,2,50,100)
print (num_list1)
print ("----------------")

num_list2 = add_test(0,0)
print (num_list2)
print ("----------------")

num_list3 = add_test()
print (num_list3)
print ("----------------")

# Using arbitrary keywords arguments
def add_test1(*numbers, **kwargs):
    print (numbers)
    print (kwargs)
    return sum(numbers) + sum(kwargs.values())

x = add_test1(1,5,10,20, k=500)
print (x)
