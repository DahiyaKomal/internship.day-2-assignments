import requests

url = "http://api.open-notify.org/iss-now.json" #given url

response = requests.get(url) # using GET to get info from the url

if response.status_code == 200:
    data = response.json()

    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']
    timestamp = data['timestamp']


    print("Latitude is:",latitude)
    print("Longitude is:",longitude)
    print("timestamp is:",timestamp)

else:
    print("An Error is found")
