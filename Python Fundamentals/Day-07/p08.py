# Problem Statement: Pass or Fail - Create a list that stores "Pass" if mark ≥ 50, "Fail" otherwise.
marks = [45, 78, 32, 90, 67]
l = ['pass' if i >=50 else 'fail' for i in marks]
print(l)
