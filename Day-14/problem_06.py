# Problem 06
# The Inventory Out-of-Stock Auditor
# 
# A warehouse system stores current stock levels in a dictionary (e.g., {"Mouse": 12, "Keyboard": 0}). Loop through the key-value pairs; extract all product names whose stock value is exactly zero and save them into a standalone list called restock_queue.


stock = {
    "Mouse": 12,
    "Keyboard": 0,
    "Monitor": 5,
    "USB Cable": 0,
    "Headset": 3,
    "Webcam": 0,
    "Desk Mat": 8,
    "HDMI Adapter": 0
}

restock_queue = [key for (key,value) in stock.items() if value == 0]
print(restock_queue)

