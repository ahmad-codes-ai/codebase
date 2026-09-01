sum = 0
count = 0
while True:
    n = int(input("Enter number: "))
    if n == 0:
        break
    else:
        sum = sum + n
        count += 1

if count > 0:
    avg = sum / count
    print(f"Sum: {sum}")
    print(f"Average: {avg}")
else:
    print("No numbers")
