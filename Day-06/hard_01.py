# Problem: Take a password string input. Use loops and string validation methods to check if it satisfies all these conditions: at least 8 characters long, contains at least one uppercase letter, one lowercase letter, one numeric digit, and one structural special character (like _, @, or #).

pas = input("Enter Your pass: ")
l = len(pas)

lo = ''
up = ''
nu = ''
sp = ''

for i in pas:
  if i.islower():
    lo +=i
  elif i.isupper():
    up+=i
  elif i.isdigit():
    nu+=i
  elif i in ['_','@','#']:
    sp+=i

if lo and up and nu and sp and l>=8:
  print("Strong Pass")
else:
  print("Not strong pass")
