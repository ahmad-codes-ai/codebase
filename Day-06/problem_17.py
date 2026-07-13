# Problem: Write a loop that scans a main string for a 2-character target substring and counts exactly how many times that substring occurs throughout the entire text without using `.count()`.

main = input("Enter main string: ")
tar = input("Enter two char target substring: ")
count = 0

lm = len(main)

for i in range(0,lm):
  m = main[i:i+2:1]

  if m == tar:
    print(f"The target appear at starting index {i}")
    count+=1
  else:
    pass

print(f"Total appearence {count}")
