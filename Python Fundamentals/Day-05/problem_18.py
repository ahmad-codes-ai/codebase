# Problem 18: Digit Extractor and Counter
# Take an alphanumeric string input (e.g., "Lahore2026"). Loop through it to count
# exactly how many numeric digits exist inside it.

s = input("Enter a alphanumeric string: ")
count = 0

for i in s:
  if i.isnumeric():
    count+=1
  else:
    pass

print(count)
