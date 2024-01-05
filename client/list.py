import requests


endpoint = "http://localhost:8000/api/products/"

response = requests.get(endpoint)
#print(response.text)
print(response.status_code)
print(response.json())