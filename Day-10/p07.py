# Problem Statement: Even or Odd - Create a list from numbers 1–10 where "Even" is stored for even and "Odd" for odd.
x = ['even' if i%2 == 0 else 'odd' for i in range(1,11)]
print(x)
