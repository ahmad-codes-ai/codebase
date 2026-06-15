# Problem 19
# The Financial Transaction Audit
# 
# A bank log contains positive floats (deposits) and negative floats (withdrawals). Loop through the transaction list, calculate the total sum of withdrawals only, and print the final value as a positive absolute number.


trans = [250.00, -45.50, 100.00, -30.00, -120.75, 500.00, -60.00, -15.25, 200.00, -80.00]
m = 0
for i in trans:
  i = str(i)
  if i.startswith('-'):
    i = float(i)
    m+=i
  else:
    pass

if m < 0:
  print(-m)
else:
  print(m)

