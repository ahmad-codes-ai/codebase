import os
from dotenv import load_dotenv   # To load env file

load_dotenv()

result = os.getenv('student','false').lower() == 'true'   # false is the default value provided in case var dosent exist

print(result)
print(type(result))

# This env is always returning a string