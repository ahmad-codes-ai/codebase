# Problem 7: The Terminal String Signal
# Write a while loop that continuously asks for user input and echoes it back,
# terminating instantly only when the user types the exact string "exit".

while True:
  user = input("Enter something: ")
  if user == 'exit':
    break
  else:
    print(user)
