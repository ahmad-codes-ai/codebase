import httpx


data = {
    'name':'Ahmad',
    'age':16,
    'weight': 56.3,
    'height': 1.68,
    'id': 'P10101',
    'city': 'lahore',
    'gender': 'Male',
    'married': False,
    'contacts': {'phone':'039496','phone2':'08213070347'},
    'allergies': ['asthama','dust']
}


response = httpx.post('http://127.0.0.1:8000/create',json=data)


print(response.status_code)
