import requests
import config

url = config.users()

data =  dict()

name = input('enter your name: ')
data['name'] = name 

email = input('enter your email: ')
data['email'] = email

status = input('status: ')
data['status'] = status 

# print(data)

headers = dict()
headers['Authorization'] = 'Bearer' + config.access_token()


response = requests.post(url, data, headers= headers)
if response.status_code == 200:
    print("POST request successful!")
    print(response.json())
else:
    print(f"Error: {response.status_code}")


