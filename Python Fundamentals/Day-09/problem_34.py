# Problem 34
# The Local Network Device Pinger
# 
# A Lubuntu automation script scans network IP addresses. Loop through a list of strings representing connected device IPs; if an IP string ends with the substring ".1", print that it is likely a network router gateway node.


ip_addresses = ["192.168.1.1", "192.168.1.45", "10.0.0.1", "172.16.0.22", "192.168.0.1", "10.0.0.67", "172.16.0.1", "192.168.1.99"]

for i in ip_addresses:
  if i.endswith('.1'):
    print("Its a router gateway")
  else:
    print("This is normal ip")






