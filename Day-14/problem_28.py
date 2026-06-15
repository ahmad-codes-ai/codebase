# Problem 28
# The Server Node Load Balancer
# 
# A system routes web traffic to three server nodes represented as keys in a dictionary containing current active connection integers. Loop through the keys to identify which specific server node currently has the lowest connection number.


servers = {
    "node_a": 23,
    "node_b": 17,
    "node_c": 31
}

lserver = ''
min = float('inf')

for (k,v) in servers.items():
  if v < min:
    min = v
    lserver = k

print(f"The server with lowest load is {lserver}")

