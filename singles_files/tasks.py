import requests

url = "https://reqres.in/api/users/3"
headers = {"x-api-key": "reqres-free-v1"}

json_put = [{"name": "morpheus",
     "job": "zion resident"}]

response = requests.put(url, json=json_put, headers=headers)
print(response.json())

url = "https://petstore.swagger.io/v2/store/order/1"

response = requests.delete(url)
print(response.json())

url = "https://reqres.in/api/users/2"

response = requests.delete(url, headers=headers)
print(response.status_code)

url = "https://reqres.in/api/users/2"
response = requests.get(url,headers=headers)
print(response.json())

url = "https://reqres.in/api/users?page=2"
response = requests.get(url,headers=headers)
print(response.json())

url = "https://reqres.in/api/users/15"
response = requests.get(url,headers=headers)
print(response.status_code)

url = "https://reqres.in/api/unknown/2"
response = requests.get(url, headers=headers)
data = response.json().get('data')
print (len(data))