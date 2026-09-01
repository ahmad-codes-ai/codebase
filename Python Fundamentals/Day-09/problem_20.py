# Problem 20
# The Git Branch Name Verifier
# 
# Open-source projects enforce strict branch naming rules. Loop through a list of developer branch names; check if each string starts with "feature/", "bugfix/", or "hotfix/". If it doesn't, print a validation failure message.


branches = [
    "feature/login-page",
    "johns-experiment",
    "bugfix/memory-leak",
    "test-branch",
    "hotfix/payment-error",
    "feature/signup-form",
    "random-branch",
    "bugfix/crash-fix",
    "my-work",
    "hotfix/security-patch"
]

valid = []
invalid = []

for i in branches:
  if i.startswith('feature/') or i.startswith('bugfix/') or i.startswith('hotfix/'):
    valid.append(i)
  else:
    invalid.append(i)

print(f"Valid Branches: {valid} \n Invalid Branches: {invalid}")

