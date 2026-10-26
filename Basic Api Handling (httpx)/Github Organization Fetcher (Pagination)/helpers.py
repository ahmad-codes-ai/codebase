import httpx
import os
import json
from dotenv import load_dotenv
from user_api import *
from github_url_extract import *



load_dotenv()


api = os.getenv('Token')


client = httpx.Client(

    base_url = 'https://api.github.com/orgs',

    headers = {
    'accept':'application/json',
    "Authorization": f"Bearer {api}"        
}, 

)




def fetch_org(name):
    path = f'/{name}/repos?per_page=100'
    count = 0
    final = []
    print('fetching.........')
    while count<100:
        
        s = call_api(client,'get',path)
        headers = s['headers']

        result = extract(r'<([^>]+)>;\s*rel=\"next\"',headers['link'])

        data = s['data']
        for i in data:

            d = {
                'name':i.get('name'),
                'stargazer_count': i.get('stargazers_count'),
                'language': i.get('language'),
                'description': i.get('description')
            }

            final.append(d)

        if result is None:
            break 

        path = result

        count+=1


    data2 = []

    for item in final:
        data2.append(item)

    with open(r'C:\Users\Lenovo\Desktop\Test Attempts\paractice 4\data.json','w') as f:
        json.dump(data2,f,indent=4)

    return final


def sort_repos():

    with open(r'C:\Users\Lenovo\Desktop\Test Attempts\paractice 4\data.json','r') as f:
        data = json.load(f)

    final = sorted(data, key=lambda x: x["stargazer_count"], reverse=True)

    with open(r'C:\Users\Lenovo\Desktop\Test Attempts\paractice 4\data.json','w') as f:
        json.dump(final,f,indent=4)


def get_sorted_repo(count=10):
    with open(r'C:\Users\Lenovo\Desktop\Test Attempts\paractice 4\data.json','r') as f:
        data = json.load(f)

    return data[0:count]
