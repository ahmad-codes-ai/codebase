# Problem: Track a robot moving on a grid with options 1-4 and compute final straight-line distance on 5
rx = 0
ry = 1

while True:
  print("--------- Robot Simulation ----------")
  print("1: UP ")
  print("2: DOWN ")
  print("3: LEFT ")
  print("4: RIGHT ")
  print("5: ! ")
  user = int(input("Enter Your choice: "))
  steps = int(input("Enter steps: "))

  if user == 1:
    ry+=steps
  elif user == 2:
    ry-=steps
  elif user == 3:
    rx-=steps
  elif user == 4:
    rx+=steps
  elif user == 5:
    distance = (rx**2 + ry**2) ** 0.5
    result = round(distance)
    print(result)
    break
  else:
    print("Invalid Input entered")
