t1 = 0
t2 = 1
count = 0
while count < 10:
    print(t1, end=" ")
    next_term = t1 + t2
    t1 = t2
    t2 = next_term
    count += 1
print()
