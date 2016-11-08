'''
The program will ask the user will for the length, width and height of a rectangular box.
The program will calculate the volume of the box and display the result.
The program will display meaningful error messages and exit gracefully in all situations.
'''

def get_user_input(*names):
    output_values = []

    for name in names:
        raw_input = input(name + ": ")
        processed_input = process_input(raw_input)
        output_values.append(processed_input)

    return output_values

def process_input(raw_input):
    '''
    Converts user input into a positive float.
    Raises ValueError if the input is non-numeric, or
    if the input is a negative number.
    '''
    try:
        value = float(raw_input)
    except ValueError:
        raise ValueError("%s is not a number" % raw_input)

    if value <= 0:
        raise ValueError("All dimensions must be greater than zero.")

    return value


def main():
    print ("This program will calculate the volume of a rectangular box given its length, width, and height.\n")

    success = False

    try:
        length, width, height = get_user_input('Length', 'Width', 'Height')
        success = True

    except ValueError as e:
        print (e)

    except KeyboardInterrupt:
        print ("\nGoodBye.")

    if success:
        total_volume = length * width * height
        print ("\nThe total volume of the box is %.2f" % total_volume)

if __name__ == "__main__":
    main()
