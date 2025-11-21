import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

data ={"userId": 11,
  "id": 100,
  "title": "South Indian",
  "boby": "Menu" }

print(requests.post(url,json=data))
print(response.status_code)
