import requests
forename = input()
response = requests.get(f'https://ws-public.interpol.int/notices/v1/red?forename={forename}&resultPerPage=200')
print(response.json()["query"]["forename"])