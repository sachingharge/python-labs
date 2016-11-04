def get_user_input():
    try:
        x = input("Enter a number: ")
        x = int(x)
        return x
    except ValueError:
        raise Exception("%s is not a number" % x)
    except KeyboardInterrupt:
        print ("\nGoodbye")
        raise

def custom_message():
    try:
        get_user_input()
    except Exception as e:
        print(e)

custom_message()
