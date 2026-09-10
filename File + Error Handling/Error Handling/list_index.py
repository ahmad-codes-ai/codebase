fruits = ["apple", "banana", "cherry"]

try:
    user = int(input("Enter the index: "))
    print(fruits[user])
except IndexError:
    print('Index out of range. Choose 0-2')
except ValueError:
    print('Plz enter a number')