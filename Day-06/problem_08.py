# Problem: Take a positive integer N from the user. Run a while loop that processes N until it reaches 1. If N is even, update it ($N = N // 2$). If N is odd, update it ($N = 3 \times N + 1$). Print N at every step and track the total number of steps taken.

n = int(input("Enter a number: "))
count = 0

while n!=1:
    if n%2 == 0:
      n = n//2
      print(n)
    else:
      n = (3*n)+1
      print(n)
    count+=1

print(f"Completed in {count} steps")
