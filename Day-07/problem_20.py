# Problem: Take a mixed alphanumeric string (e.g., "Py3th1o6n"). Loop through it character by character, isolate the numeric digits, explicitly convert them to integers, and calculate their final collective sum.

s = "Py3th1o6n,1"
m = 0

for i in s:
  if i.isdigit():
    i = int(i)
    m = (m*10)+i
  else:
    pass

m = str(m)
sum = 0
for i in m:
  i = int(i)
  sum+=i

print(f"The sum of digits in this alphanumeric string is : {sum}")
