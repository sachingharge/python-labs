# simple add function
def add(a, b):
    return a + b

x = add(1, 2)
print(x)

# optional argument
def optional_add(a, b=0):
    return a + b
a = optional_add(1, 10)
print(a)

# mutable objects
def append_zero(lst=[]):
    lst.append(0)
    return lst

l = append_zero()
#k = append_zero()
print(l)

def append_zero1(lt1=None):
    if lt1 is None:
        lt1 = []
        lt1.append(0)
    else:
        lt1.append('2')
    return lt1

a = append_zero1()
print(a)
b = append_zero1()
print(b)
print(a is b)
a_id = id(a)
print("a id is:", a_id)
b_id = id(b)
print("b id is:", b_id)
c = append_zero1(['1', '3', '5'])
print(c)
