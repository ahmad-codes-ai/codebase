# Problem 14: Even Position Caps
# Extract all characters sitting at even index positions of a string, convert that
# specific slice to all uppercase letters, and print it.

s = input("Enter a string: ")

ns = s[0::2]
ns = ns.upper()
print(ns)
