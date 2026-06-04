n = int(input("Enter N: "))
i = 1
sum = 0
while i <= n:
    if i % 5 != 0:
        if (sum + i >= 300) or sum >= 300: 
            break
        else:
            sum = sum + i
    i += 1
print(f"{sum}")
