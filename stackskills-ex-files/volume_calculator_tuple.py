'''
The program will ask the user will for the length, width and height of a rectangular box.
The program will calculate the volume of the box and display the result.
The program will display meaningful error messages and exit gracefully in all situations.
'''

def get_user_input(length, width, height):
    input_length = input("Enter length value : ")
    length_value = input_length
    input_width = input("Enter width value : ")
    width_value = input_width
    input_height = input("Enter height value : ")
    height_value = input_height

    tupple_value = ('length_value', 'width_value', 'input_height')
    print (tupple_value)

    #try:
    float_check = tupple_value
    #except ValueError:
    #    raise ValueError("%s is not a number" % float_check)

    #if float_check <= 0:
    #    raise ValueError("All dimensions must be greater than zero.")

def main():
    print ("This program will calculate the volume of a rectangular box given its length, width, and height.\n")

    sucess = False

    try:
        length, width, height = get_user_input('Length', 'Width', 'Height')
        sucess = True

    except ValueError as e:
        print (e)

    except KeyboardInterrupt:
        print ("\nGoodBye.")


if __name__ == "__main__":
    main()
