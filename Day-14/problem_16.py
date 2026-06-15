# Problem 16
# The Smart-Home Temperature Logger
# 
# A server tracks connected room temperatures as integers. Loop through the list of temperatures; calculate the mathematical average temperature of the house, and print an alert if the average drops below 18°C.


temperatures = [22, 19, 21, 18, 20, 17, 23, 19, 18, 16, 21, 20]
sum = 0

for i in temperatures:
  sum+=i

avg = sum / len(temperatures)

if avg < 18:
  print("Warning avg temp is below 18°C")
else:
  print(f"Avg temp is: {avg} and its fine")

