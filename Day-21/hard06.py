"""
### 6. System Feature: Financial Ledger Reconciler & Overdraft Quarantine

**Context:** A database node failed mid-settlement, risking transaction corruption. The core billing module must step through an array of peer-to-peer balance modifications. The runtime state must keep track of absolute account values; if an account balance is calculated to drop below zero at any point in the pipeline, that specific sequence step must be rejected, quarantined in an audit log, and its balance adjustments reversed immediately.

**Input State:**
```python
balances = {"Ahmad": 100, "Ali": 50}
transactions = [("Ahmad", "Ali", 30), ("Ali", "Ahmad", 100)]
```

**Expected Output State:**
```python
final_balances = {"Ahmad": 70, "Ali": 80}
fraud_quarantine = [("Ali", "Ahmad", 100)]
```
"""

balances = {"Ahmad": 100, "Ali": 50}
transactions = [("Ahmad", "Ali", 30), ("Ali", "Ahmad", 100)]

fraud_quarantine = []

for i,j,k in transactions:
  if k <= balances[i]:
    balances[i]-=k
    balances[j]+=k
  else:
     s = (i,j,k)
     fraud_quarantine.append(s)

print(balances)
print(fraud_quarantine)
