# import httpx
# import os 


# # response = httpx.get("https://jsonplaceholder.typicode.com/users/1")  # This gives us a object

# '''
# print(response.status_code)  # Print status code
# print(response.json()) # Return the json data
# print(response.text)  # Return the text reponse its str not json look like json
# print(response.url)   # Give the final url
# '''




# '''
# print(response.request)  # This tell what we our program (client) sent to the server include method and path
# print(response.request.url)  # This contain url we requested
# print(response.request.headers)  # httpx auto send this info

# '''



# # response2 = httpx.get("https://jsonplaceholder.typicode.com/posts",params={'userId':3})

# # print(response2.request.url)  # Can use this to get the final url going. Usefull for debuggin


# # if response2.status_code == 200:
# #     posts = response2.json()
# #     print(type(posts))
# #     print(f"Length of user {posts[0]['userId']} post is: {len(posts)}")

# #     for post in posts:
# #         print(post)
# #         print()

# # else:
# #     print("Error Fetching")



# response = httpx.post(
#     "https://httpbin.org/post",
#     json={"name": "Ahmad", "age": 16},
# )

# print(response.status_code)
# print(response.json())


# print()

# response2 = httpx.post(
#     "https://httpbin.org/post",
#     json={"name": "Ali", "age": 19},
# )

# print(response2.status_code)
# print(response2.json())


# print()
# print('Now seeing what it have')


# response3 = httpx.get("https://httpbin.org/post")


# print(response3.status_code)
# print(response3.json())



import httpx

# Simulating "the server said the user already exists"
response = httpx.get("https://httpbin.org/status/409")

print("Status:", response.status_code)   # 409
print("Body:", response.text)            # empty