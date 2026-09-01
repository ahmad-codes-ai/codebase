n = int(input("Enter number: "))
rev = ''
while n > 0:
    last = n % 10
    n = n // 10
    rev = rev + str(last)
rev = int(rev)
print(f"{rev}")
