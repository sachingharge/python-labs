#
# Example file for working with conditional statements
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

def main():
  x, y = 100, 100


# conditional flow uses if, elif and else
  if ( x < y):
    st = "x is less than y"
  elif ( x == y):
    st = "x is same as y"
  else:
    st = "x is grater than y"
  print (st)

# condtional statements let you use "a if C else b"
  st = "x is less that y!!" if ( x < y) else "x is greater than or equal to y"
  print (st)
if __name__ == "__main__":
  main()
