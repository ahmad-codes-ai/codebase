"""
### 45. The Sub-String Frequency Checker

Given a long text string and a shorter search string variable, write a loop that steps through the long text string chunk by chunk to count exactly how many times the short substring appears consecutively.
"""

l = "abababab"
s = "ab"
count = 0
k = len(s)

for i in range(0,len(l)):
  m = l[i:i+k]
  if m == s:
    count+=1

print(count)
