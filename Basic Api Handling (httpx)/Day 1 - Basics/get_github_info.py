import httpx

def get_user_github_info(username):
  response = httpx.get(f"https://api.github.com/users/{username}")

  if response.status_code == 200:
    data = response.json()
    print(f"The user is found his name is: {data['name']} and have {data['followers']} followers.")
    print(f"{data['name']} has total {data['public_repos']} public repos.")
    l = data['created_at'].split('-')
    date,month,year = l[-1][:2],l[1],l[0]
    print(f"{data['name']} account was created on: {date}-{month}-{year}")

  elif response.status_code == 404:
    print("Error 404")
    print("User Not Found")

  else:
    print(f"Error {response.status_code}")


user_name = input("Enter the Github username: ")
get_user_github_info(user_name)