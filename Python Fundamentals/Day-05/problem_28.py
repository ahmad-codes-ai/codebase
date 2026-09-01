# Problem 28: Dynamic Sentence Builder
# Take three separate inputs: a project name, a programming language, and a day number.
# Use the .format() method to print them inside a structured update sentence.

pname = input("Enter Project name: ")
plang = input("Enter a programming language: ")
day = input("Enter day number: ")

print("You will make {} project using {} language on {}".format(pname,plang,day))
