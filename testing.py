import requests
response = requests.get('https://randomuser.me/api')
print(response.json()['results'][0]['name']['title'])