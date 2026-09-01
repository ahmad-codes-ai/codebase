import random

# Exercise 1: Print a multiplication table using a while loop
print("--- Multiplication Table ---")
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    m = n * i
    print(f"{n} x {i} = {m}")
    i += 1

print("\n--- Town Population Growth Simulation ---")
# Exercise 2: Town population growth tracker (10% increase year over year)
pop = 10000
inc = 0.10
for year in range(1, 11):
    m = pop * inc
    pop = pop + m
    print(f"The population after year {year} = {pop:.2f}")

print("\n------ Welcome to Number Guessing Game --------")
# Exercise 3: Number Guessing game using while True and break
count = 0
target = random.randint(0, 100)

while True:
    user = int(input("Enter a Number: "))
    count += 1
    if user == target:
        print(f"Congratulations! You guessed the correct number: {target} in {count} attempts")
        break
    elif user > target:
        print(f"{user} is bigger than the target, go down")
    elif user < target:
        print(f"{user} is less than the target, move up")
