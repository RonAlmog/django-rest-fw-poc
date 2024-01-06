import requests


endpoint = "http://localhost:8000/api/products/4/update/"
data={
    "title": "hello title my old friend",
    "price": 129.99,
    "content": "Wiiiii"
}
response = requests.put(endpoint, json=data)
#print(response.text)
print(response.status_code)
print(response.json())