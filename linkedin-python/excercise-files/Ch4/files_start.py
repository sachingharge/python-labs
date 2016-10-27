#
# Read and write files using the built-in Python file methods
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

def main():
    # Open a file for writing and create it if it doesn't exist
    f = open("sachin.txt", "w+")

    # Open the file for appending text to the end
    #f = open("sachin.txt","a+")

    # write some lines of data to the file
    for i in range(5):
        f.write("This is Sachin Test %d\r\n" % (i+1))

    # close the file when done
    f.close()

    # open file and read the content
    f = open("sachin.txt", "r")

    if f.mode == 'r': # check to make sure that the file was opened
        # use the read() function to read the entire file
        #contents = f.read()
        #print (contents)

        fl = f.readlines() # readlines reads the individual lines into a list
        for x in fl:
            print (x)

if __name__ == "__main__":
  main()
