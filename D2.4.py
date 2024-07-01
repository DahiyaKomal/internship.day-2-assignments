import requests

url="http://api.open-notify.org/iss-now.json"

response = requests.get(url)

if response.status_code==200:
    print("Here is your response")
    print(response.json())
else:
    print("An Error is found")
