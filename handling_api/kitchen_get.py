import requests
import config

url = config.users()
print(url)
response = requests.get(url)
data = response.json()

# print(data)

conn = data['data']['headers']['host']
print(conn)
