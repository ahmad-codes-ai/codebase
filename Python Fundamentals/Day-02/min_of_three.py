# Find the minimum of three numbers using logical operators
n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
n3 = int(input("Enter n3: "))

if n1 < n2 and n1 < n3:
    min_num = n1
elif n2 < n1 and n2 < n3:
    min_num = n2
else:
    min_num = n3

print(f"The smallest number among them is : {min_num}")
