"""
### 8. System Feature: Academic Gradebook Normalizer & Attendance Penalty Engine

**Context:** The school board has updated its data reporting requirements. The database contains historical arrays of student scores grouped by track. The transformation pipeline must loop through the nested dataset, substitute the lists of raw integers with a single calculated floating-point average value, inspect performance states, and dock the global attendance record by a strict 10% penalty if any subject average drops below the passing threshold.

**Input State:**
```python
gradebook = {"stud_1": {"subjects": {"CS": [40, 40], "Math": [90, 90]}, "attendance": 90}}
```

**Expected Output State:**
```python
updated_gradebook = {"stud_1": {"subjects": {"CS": 40.0, "Math": 90.0}, "attendance": 81}}
```
"""

gradebook = {
    "stud_1": {"subjects": {"CS": [40, 40], "Math": [90, 90]}, "attendance": 90},
    "stud_2": {"subjects": {"CS": [75, 80], "Math": [70, 30]}, "attendance": 85}
}

updated_gradebook = {}

for i in gradebook:
  s = gradebook[i]['subjects']
  a = gradebook[i]['attendance']
  flag = False
  for j in s:
    m = gradebook[i]['subjects'][j]
    avg = sum(m) / len(m)
    if avg <= 40:
      flag = True
    if i not in updated_gradebook:
      updated_gradebook[i] = {'subjects' : {j : avg} , 'attendance' : a}
    else:
      updated_gradebook[i]['subjects'][j] = avg

  if flag:
    a = a * 0.90

    updated_gradebook[i]['attendance'] = a

print(updated_gradebook)
