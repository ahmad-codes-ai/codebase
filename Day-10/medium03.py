"""
### 3. The Smart-Contract Gas Fee Auditor

A crypto wallet tracker monitors transaction logs as a list of dictionaries, where each dict has a "gas_price" and a "status". Loop through the transactions; if the status is "SUCCESS", accumulate the gas price into a running sum. If it's "FAILED", skip it but log the index.
"""

transactions = [
    {"gas_price": 25, "status": "SUCCESS"},
    {"gas_price": 15, "status": "FAILED"},
    {"gas_price": 30, "status": "SUCCESS"},
    {"gas_price": 10, "status": "FAILED"},
    {"gas_price": 25, "status": "SUCCESS"}
]
idx = 0
sum = 0
fail = []
for i in transactions:
  if i['status'] == 'SUCCESS':
    sum+= i['gas_price']
  else:
    fail.append(idx)
  idx+=1

print(sum)
print(fail)
