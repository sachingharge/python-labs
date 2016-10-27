# integer checks
x = 3
y = 1

if x == 1 and y == 2:
    print("x is 1 and y is 2")

if x == 1 or y == 2:
    print("x is 1 or y is 2")

#var1 = 2
var1 = 0
if var1:
    print("var1: Got a true expression value")
    print (var1)
else:
    print("var1: Got a false expression value")
    print (var1)

# string checks
#var2 = "a"
var2 = ""

if var2:
    print("var2: Got a non empty sequence is like true")
    print(var2)
    print("===================================================")
else:
    print("var2: Got a emptry squence is like false")
    print(var2)
    print("===================================================")


# float checks
var3 = 0.0
var4 = 0.1
var5 = -0.1

if var3:
    print("var3: float value 0.0 is not considered to true")
    print(var3)
    print("===================================================")
else:
    print("var3: Got a float value 0.0")
    print(var3)
    print("===================================================")

if var4:
    print("var4: Got a float value considered to be true")
    print(var4)
    print("===================================================")
else:
    print("exiting")
    print(var4)
    print("===================================================")

if var5:
    print("var5: Got a negtive float value considered to be true")
    print(var5)
    print("===================================================")
else:
    print("exiting")
    print(var5)
    print("===================================================")
