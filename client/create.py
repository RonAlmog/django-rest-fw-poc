import requests


endpoint = "http://localhost:8000/api/products/"

data={
    "title":"title is good",
    "price": 32.99
}
response = requests.post(endpoint, json=data)
#print(response.text)
print(response.status_code)
print(response.json())