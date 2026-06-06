# Problem 3: The Modulus Validation
# Take two integer inputs, A and B. Check if A is completely divisible by B.
# Print a clean message like "Divisible: True" or "Divisible: False".


a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
if a % b == 0:
    print("Divisible: True")
else:
    print("Divisible: False")
