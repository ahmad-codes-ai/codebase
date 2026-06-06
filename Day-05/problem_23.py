# Problem 23: URL Border Patrol
# Check if a user-submitted URL string starts with "https://" and ends with ".com".
# Print a valid or invalid message based on the result.

s = input("Enter a url: ")

if s.startswith('https://') and s.endswith('.com'):
  print("Valid url")
else:
  print("Invalid Url")
