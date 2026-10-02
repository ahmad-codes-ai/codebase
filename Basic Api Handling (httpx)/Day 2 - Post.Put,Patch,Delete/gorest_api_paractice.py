import httpx
import os
from dotenv import load_dotenv


load_dotenv()

API = os.getenv("Token",None)


response = httpx.get('https://gorest.co.in/public/v2/users')

if response.status_code == 200:
    data = response.json()
    for user in data:
        print(f"{user.get('id')} | {user.get('name')}")
else:
    print(response.status_code)



payload = {
    "name": "Pranav Kapoors",
    "email": f"pranav44445554-@example.com",   # 422 error came when email already exist
    "gender": "male",
    "status": "active",
}


headers = {
    'Authorization' :f"Bearer {API}",     # This is must here 
    'Content-Type' : 'application/json',
    'Accept': 'application/json'
}




response2 = httpx.post('https://gorest.co.in/public/v2/users',json=payload,headers=headers)


if response2.status_code == 201:
    data = response2.json()
    print(data)

else:
    print(response2.status_code)
    print(response2.json())



response3 = httpx.get('https://gorest.co.in/public/v2/users/8646101',headers=headers)   # Required authetication

if response3.status_code == 200:
    print(response3.json())
else:
    print(response3.status_code)



new_data = {'City':'Lahore','gender':'female'}
response4 = httpx.put('https://gorest.co.in/public/v2/users/8646101',headers=headers,json=new_data)

# In this api the put is working same as patch bcz the server has wrote that logic.
print(response4.status_code)
print(response4.json())


new_data = {'City':'Lahore','name':'Ahmad'}
response5 = httpx.put('https://gorest.co.in/public/v2/users/8646101',headers=headers,json=new_data)

# Same with patch

print(response5.status_code)
print(response5.json())


response6 = httpx.delete('https://gorest.co.in/public/v2/users/8646101',headers=headers)

print(response6.status_code)

# Normally delete return 204 means no message so response6.json() will give error



# Now need to build proper system with this 

# Add user to this db
# Get users / user
# Update a user data
# Delete a user


# All must be done properly with unexpected scnerios and 4xx status code handling




