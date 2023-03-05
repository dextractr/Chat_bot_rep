import requests

api_url = 'http://numbersapi.com/'

num = 43

response = requests.get(api_url+ str(num))

if response.status_code == 200:
    print(response.text)
else:
    print(response.status_code)