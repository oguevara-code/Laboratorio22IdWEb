import requests

url = "https://httpbin.org/get"
response = requests.get(url)

data = response.json()

print("IP:", data.get("origin"))
print("Headers:", data.get("headers"))
print("Args:", data.get("args"))