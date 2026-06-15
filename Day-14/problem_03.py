# Problem 03
# The Product Pricing Matrix Lookup
# 
# You are setting up a checkout counter for a micro-startup. Create a dictionary containing four items and their integer prices; take a user input string, check if that item exists in your dictionary, and print its price or an error message if missing.


inventory = {
    "laptop": 800,
    "phone": 500,
    "charger": 25,
    "earbuds": 60
}

user = input("Enter name of item to check its price / availability : ").lower()

print(inventory.get(user,"This item is not in the inventory"))

