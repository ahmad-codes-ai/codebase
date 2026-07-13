# Problem: Take inputs for age and matric_marks (percentage). If age is greater than 15, nest another conditional: if marks are $\ge 80\%$, print "Admitted: ICS-AI"; if marks are between $60\%$ and $79\%$, print "Admitted: General Track"; else print "Ineligible due to marks". If age is 15 or less, print "Ineligible due to age".

age = int(input("Enter Your age: "))
mm = int(input("Enter matric marks percentage: "))

if age > 15:
  if mm >= 80:
    print("Admitted: ICS-AI")
  elif mm >= 60:
    print("Admitted: General Track")
  else:
    print("Ineligible due to marks")
else:
  print("Ineligible due to age")
