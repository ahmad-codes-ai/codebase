# Menu Driven Calculator using structural conditional matching
a = int(input("Enter n1: "))
b = int(input("Enter n2: "))
op = input("Enter your operator: ")

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
elif op == '%':
    print(a % b)
elif op == '**':
    print(a ** b)
else:
    print("Invalid Input Given")
