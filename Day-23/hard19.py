"""
### 19. Core Logic: Pure Arithmetic Digit-Reversal Numerical Validator

**Context:** Low-level assembly controllers need to verify serial integer patterns. Without transforming integers into text representations or strings, the validator loop must isolate individual numbers, extract positional digits via arithmetic division algorithms, and identify which numeric profiles read identically forward and backward.

**Input State:**
```python
numbers = [121, 456, 8998]
```

**Expected Output State:**
```python
palindromes = (121, 8998)
```
"""

numbers = [121, 456, 8998]
palindromes = []

for i in numbers:
  m = 0
  s = i
  while i!=0:
    l = i%10
    m = (m*10)+l
    i = i//10

  if m == s:
    palindromes.append(s)

print(palindromes)
