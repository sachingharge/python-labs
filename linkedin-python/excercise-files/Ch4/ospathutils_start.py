#
# Example file for working with os.path module
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    # print name of the OS
    print (os.name)

    # Check for item existence and type
    print ("Item exists: " + str(path.exists("sachin.txt")))
    print ("Item is file: " + str(path.isfile("sachin.txt")))
    print ("Item is directory: " + str(path.isdir("sachin.txt")))

    # Work with file paths
    print ("Item's path: "  + str(path.realpath("sachin.txt")))
    print ("Item's path and name: " + str(path.split(path.realpath("sachin.txt"))))

    # Get the modification time
    t = time.ctime(path.getmtime("sachin.txt"))
    print (t)
    print (datetime.datetime.fromtimestamp(path.getmtime("sachin.txt")))
    print ("======================================================")
    # calcualate how long time ago the item was modified
    current_time = datetime.datetime.now()
    print (current_time)
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("sachin.txt"))
    print ("It has been " + str(td) + "since the file was modified")
    print ("In Seconds: " + str(td.total_seconds()))

if __name__ == "__main__":
  main()
