"""
### PROBLEM 2: Flexible Greeting
Create a function `greet_multiple()` that:

* Takes a required greeting string
* Takes any number of `*names`
* Takes an optional separator defaulting to ", "
* Prints greeting for each name (e.g., "Hello Alice", "Hello Bob")
"""

def greet_multiple(greeting,*names,sep=', '):
  for i in names:
    print(f"{greeting}{sep}{i}")

greet_multiple('Hello','Ahmad','Ali')
