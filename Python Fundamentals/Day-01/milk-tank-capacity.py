"""
Task: Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.
Input:
Dimensions of the milk tank: H = 20cm, L = 20cm, B = 20cm
Dimensions of the glass: h = 3cm, r = 1cm
"""

h = float(input("Enter height of milk tank: "))
w = float(input("Enter width of milk tank: "))
b = float(input("Enter breadth of milk tank: "))

vt = h * w * b

vg = float(input("Enter volume of glass: "))

glass = vt // vg

print(f"Total glasses that can be make : {glass}")
