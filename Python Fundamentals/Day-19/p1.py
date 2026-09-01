"""
### PROBLEM 1: Basic Calculator
Create a function `calculate()` that:

* Takes two required numbers `a` and `b`
* Takes an optional operation defaulting to "add"
* Returns the result

(Use if/elif for add, subtract, multiply, divide)
"""

def calculate(a,b,op='+'):

  if op == '+':
    return a + b
  elif op == '-':
    return a - b
  elif op == '/':
    return a / b
  elif op == '*':
    return a*b

print(calculate(20,10))
