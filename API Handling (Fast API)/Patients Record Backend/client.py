import httpx

response = httpx.delete('http://127.0.0.1:8000/delete/P10101')


print(response.status_code)
print(response.json())
