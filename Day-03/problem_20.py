''' Problem 20: Take 5 numbers from the user one by one inside a loop. Without using any built-in
 functions, find and print the maximum (largest) number entered out of those 5. '''

max = 0
i = 1

while i<=5:
  n = int(input("Enter a number: "))
  if n > max:
    max = n
  else:
    pass
  i+=1
print(f"The largest number is : {max}")
