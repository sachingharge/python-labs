#
# Example file for parsing and processing JSON
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

import urllib2
import json

def printResults(data):
  # use the json module to load the string data into a dict
  theJSON = json.loads(data)
  print ("=============================================")
  print (theJSON)

  # now we can access the contents of the JSON like any other Python object
  if "title" in theJSON["metadata"]:
     print (theJSON["metadata"]["title"])

  # output the number of events, plus the magnitude and each event name
  count = theJSON["metadata"]["count"];
  print (str(count) + "events recorded!!!")

  # for each event, show the place where it occured
  for i in theJSON["features"]:
      print (i["properties"] ["place"])

  # print the events that only have a magnitude greater than 4
  for i in theJSON["features"]:
      if i["properties"]["mag"] >= 4.0:
          print ("%2.1f" % i["properties"]["mag"], i["properties"]["place"])

  # print only the events where at least 1 person reported feeling something
  print ("Events that were felt:")
  for i in theJSON["features"]:
      feltReports = i["properties"]["felt"]
      if (feltReports != None):
          if (feltReports > 0):
             print ("%2.1f" % i["properties"]["mag"], i["properties"]["place"], "reported: " + str(feltReports) + " times")

def main():
  # define a variable to hold the source URL
  # In this case we'll use the free data feed from the USGS
  # This feed lists all earthquakes for the last day larger than Mag 2.5
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

  # open the URL and read the data
  WebUrl = urllib2.urlopen(urlData)
  print (WebUrl.getcode())

  if (WebUrl.getcode() == 200):
      data = WebUrl.read()
      print(data)
      # print out our customized results
      printResults(data)
  else:
      print ("Received an error from server, can not retrive data " + str(WebUrl.getcode()))

if __name__ == "__main__":
  main()
