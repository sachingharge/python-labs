def get_user_input():
    x = input("Enter a number: ")
    x = int(x)
    return x

def try_except():
    try:
        x = get_user_input()
        print (x)
    except:
        print ("error, enter valid number")

    print ("Exiting try_except function")

def try_except_finally():
    try:
        x = get_user_input()
        print (x)
    except:
        print ("error, enter valid number")
    finally:
        print("Finally")

    print ("Exiting try_except_finally function")


def try_finally():
    try:
        x = get_user_input()
        print (x)
    finally:
        print ("finally testing")

    print ("Exiting try_finally function")

try_finally()
