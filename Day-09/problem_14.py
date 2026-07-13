# Problem 14
# The Bug Tracker Priority Filter
# 
# A developer dashboard tracks active software bugs in a dictionary where the bug ID is the key and the value is its severity tier ("High", "Medium", "Low"). Loop through it and extract only the bug IDs marked as "High" into a new list.


bugs = {
    "BUG-1001": "Medium",
    "BUG-1002": "High",
    "BUG-1003": "Low",
    "BUG-1004": "High",
    "BUG-1005": "Medium",
    "BUG-1006": "Critical",
    "BUG-1007": "High",
    "BUG-1008": "Low",
    "BUG-1009": "High",
    "BUG-1010": "Medium"
}

l = [key for (key,value) in bugs.items() if value.lower() == 'high']
print(l)

