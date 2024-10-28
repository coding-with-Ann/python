import requests
import config

url = config.users()

headers = dict()
headers['Authorization'] = 'Bearer' + config.access_token()
response = requests.put(url, headers = headers)

print(response.status_code)
print(response.json())         