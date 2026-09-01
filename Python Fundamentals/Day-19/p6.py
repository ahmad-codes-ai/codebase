"""
### PROBLEM 6: User Profile
Create a function `create_profile()` that:

* Takes required `username`
* Takes any number of `*interests`
* Takes any number of `**details` (like age, city, email)
* Returns a dictionary with username, interests (tuple), and details
"""

def create_profile(username,*intrests,**details):
  s = f"The user {username} is intrested in {intrests} and his other details are as follows: {details}"
  return s

print(create_profile('ahmad.ai','python','ai',city='lahore',age=14))
