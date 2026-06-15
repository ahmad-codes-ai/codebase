# Problem 21
# The User Access Permission Guard
# 
# An authorization module uses a tuple to store non-changing system administrator user names. Take a string input from a user login attempt, check if that username exists within the tuple, and print access granted or denied.


admin = ("alice_admin", "bob_sysop", "charlie_root", "diana_netops")
user = input("Enter your username: ")

if user in admin:
  print("Access Granted")
else:
  print("Access Denied")

