# Problem 10
# The SaaS Monthly Revenue Compiler
# 
# A software company has user IDs mapped to their monthly tier fees in a dictionary. Loop through all the values in the dictionary and compute the total sum to figure out the company's current Monthly Recurring Revenue (MRR).


user_fees = {
    "user_001": 15.99,
    "user_002": 9.99,
    "user_003": 0.00,
    "user_004": 29.99,
    "user_005": 9.99,
    "user_006": 49.99,
    "user_007": 0.00,
    "user_008": 15.99,
    "user_009": 9.99,
    "user_010": 99.99
}

mrr = 0

for (key,value) in user_fees.items():
  mrr+=value

print(f"Your Total MRR is : {mrr}")

