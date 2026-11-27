import httpx



new_data = {
    'age':18,
    'weight':67,
    'city':'Karachi'
}

response = httpx.put('http://127.0.0.1:8000/edit/P10101',json=new_data)


print(response.status_code)
print(response.json())
