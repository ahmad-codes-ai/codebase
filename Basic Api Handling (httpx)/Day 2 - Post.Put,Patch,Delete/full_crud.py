import httpx
import os
from dotenv import load_dotenv

load_dotenv()


base_url = 'https://gorest.co.in/public/v2'
API = os.getenv('Token')


headers = {
    'Authorization': f"Bearer {API}",
    'Accept': 'application/json',
    'Content-Type': 'application/json'
    }


def add_user(name,email,gender='male',status='active'):

    data = {
        'name':name,
        'email':email,
        'gender':gender,
        'status':status
    }



    response = httpx.post(f"{base_url}/users",json=data,headers=headers)

    if response.status_code == 201:
        d = {'success': True, 'status_code': response.status_code, 'Id': response.json().get('id')}
    else:
        d = {'success':False, 'status_code': response.status_code}
        
    return d


def get_user(id):
   
    response = httpx.get(f"{base_url}/users/{id}",headers=headers)

    if response.status_code == 200:
      d = {
           'success':True,
           'status_code':response.status_code,
           'data':response.json()
       }

    else:
       d = {
           'success':False,
           'status_code':response.status_code,
           'data':None,
       }
    
    return d


def get_all_users():
    response = httpx.get(f"{base_url}/users",headers=headers)
    data = response.json()
    return data


def update_user(id,data={}):
    response = httpx.put(f"{base_url}/users/{id}",json=data,headers=headers)
    
    if response.status_code == 200:
        d = {
            'success':True,
            'new_data':response.json()
        }
        
    else:
        d = {
            'success':False,
            'new_data':None
        }
        
    return d


def delete_user(id):
    resposne = httpx.delete(f"{base_url}/users/id",headers=headers)
    
    if resposne.status_code == 200:
        d = {
            'success': True,
            'status_code':resposne.status_code
        }
    else:
        d = {
            'success':False,
            'status_code':resposne.status_code
        }
        
    return d


def run():
    is_running = True
    while is_running:
        print("1: Create User")
        print("2: Update User")
        print("3: List all Users")
        print("4: Get User Data")
        print("5: Exit")
        
        user = int(input("Enter Your Choice: "))
        
        
        if user == 1:
            name = input("Enter name: ")
            email = input("Enter email: ")
            gender = input("Enter gender: ")
            status = input("Enter status: ")
            
            result = add_user(name,email,gender,status)
            print(result)
            
        elif user == 2:
            id = input("Enter user Id: ")
            data = dict(input("Enter new data: "))
            
            result = update_user(id,data)
            print(result)
            
        elif user == 3:
            result = get_all_users()
            print(result)
            
        elif user == 4:
            id = input("Enter user ID: ")
            result = get_user(id)
            print(result)
            
        elif user == 5:
            id = input("Enter user ID to delete: ")
            result = delete_user(id)
            print(result)
            
        elif user == 6:
            print("Exiting")
            is_running = False
            
        else:
            print("Invalid Input")
            
            
run()