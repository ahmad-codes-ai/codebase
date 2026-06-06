# Problem 4: The Truthiness Test
# Take a raw string input. Use logical evaluation (if string:) to print "Valid Input"
# if it contains text, and "Empty Placeholder" if the user just pressed enter without typing.

s = input("Enter a string: ")

if s:
  print("Valid Input")
else:
  print("Empty placeholder")
