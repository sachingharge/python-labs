#
# Example file for retrieving data from the internet
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

import urllib2

def main():
    # open a connecton to URL using urllib
    webUrl = urllib2.urlopen("https://www.google.se/")

    # get the result code and print it
    print ("HTTP result code: " + str(webUrl.getcode()))

    # read the data from the URL and print it
    html_page = webUrl.read()
    print (html_page)

if __name__ == "__main__":
  main()
