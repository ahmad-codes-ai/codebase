"""
### PROBLEM 4: Student Report
Create a function `student_report()` that:

* Takes required `name` and `grade`
* Takes any number of `*subjects`
* Takes optional `school` defaulting to "Unknown"
* Prints a formatted report with all information
"""

def student_report(name,grade,*subjects,school='Unknown'):
  subjects_str = ', '.join(subjects)
  print(f"{name} reads in class {grade} at {school} school and has {subjects_str} subjects")

student_report('Ahmad',10,'math','cs',school = 'IS')
