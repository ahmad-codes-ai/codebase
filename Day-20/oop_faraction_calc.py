class Fraction:

  def __init__(self,x,y):
    self.num = x
    self.den = y

  def __str__(self):
    return f"{self.num}/{self.den}"

  def __add__(f1,f2):
    new_num = (f1.num*f2.den) + (f1.den * f2.num)
    new_den = f1.den*f2.den 

    return f"{new_num}/{new_den}"

  def __sub__(f1,f2):
     new_num = (f1.num*f2.den) - (f1.den * f2.num)
     new_den = f1.den*f2.den 

     return f"{new_num}/{new_den}"

  def __mul__(f1,f2):
    new_num = f1.num*f2.num
    new_den = f1.den*f2.den 

    return f"{new_num}/{new_den}"

  def __truediv__(f1,f2):
    new_num = f1.num*f2.den
    new_den = f1.den*f2.num

    return f"{new_num}/{new_den}"

f1 = Fraction(8,4)
f2 = Fraction(4,6)
print(f1+f2)
print(f1-f2)
print(f1*f2)
print(f1/f2)