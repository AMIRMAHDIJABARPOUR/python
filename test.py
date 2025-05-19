import requests

param = {"id": 3}
x = requests.get("https://jsonplaceholder.typicode.com/users", params=param)

if x.status_code == 200:
    xj = x.json()
    print(xj)
