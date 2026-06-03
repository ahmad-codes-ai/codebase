# Sum of a three-digit number without loops using % 10 and // 10
num = int(input("Enter a 3 digit number: "))

a = num % 10
num = num // 10

b = num % 10
num = num // 10

c = num

print(f"Sum of the digits: {a + b + c}")
