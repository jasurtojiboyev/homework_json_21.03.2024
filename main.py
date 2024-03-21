import requests
import json

endpoints = ["posts", "comments", "todos"]

for endpoint in endpoints:
    response = requests.get(f"https://jsonplaceholder.typicode.com/{endpoint}")
    data = response.json()
    with open(f"{endpoint}.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)
