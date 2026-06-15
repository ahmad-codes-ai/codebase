# Problem 29
# The LLM Token Usage Flag
# 
# High token limits cost money. Loop through a list of integers representing token allocations used per agent execution; if any single run hits exactly 4096 tokens, break the loop immediately and print an out-of-bounds warning.


token_allocations = [2048, 1024, 4096, 3000, 512, 4096, 8192]

for i in token_allocations:
  if i == 4096:
    print("out-of-bounds")
    break

