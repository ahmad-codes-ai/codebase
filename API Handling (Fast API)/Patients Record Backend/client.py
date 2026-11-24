import httpx

response = httpx.get('http://127.0.0.1:8000/sort',params={'sort_by':'height','order':'desc'})


if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code)