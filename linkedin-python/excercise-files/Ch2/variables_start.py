#
# Example file for variables
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

# declare a variable and intialize it
f = 0
print (f)

# re-declaring the variable works

#f = "abcd"
#print (f)

# ERROR: variables of different types can not be combined
#print "string type" + 123

#print ("string type " + str(1234))

# Global vs local variables in functions
def somefunction():
    global f
    f = "def"
    print (f)

somefunction()
print (f)

#un declare or remove variable value
del f
print (f)
