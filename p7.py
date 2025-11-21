import requests
import json

#GET API
#I got API Link from reqres Website .
response = requests.get("https://reqres.in/api/users")
#response.statusCode gives 200 means success
#response.statusCode gives 404 or any other number means error
print("Get Status" , response.status_code)
assert response.status_code == 200
#print statement retrieves how many users are available
print("Total Users Found", len(response.json()["data"]))


# POST API using jsonplaceholder (mock API)
#I tried on reqres website but post api is not working , so jsonplaceholder api is working so I used this One.
payload = {"name": "Satish", "Job": "Lead Engineer"}

# Send POST request with JSON payload
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)

# Print status code (201 means "Created")
print("Post Status:", response.status_code)

# Print the mock response (includes your data + a fake ID)
print("Created Post:", response.json())

# Note: jsonplaceholder does not store data permanently.
# You won't see this post if you try to retrieve it later.

