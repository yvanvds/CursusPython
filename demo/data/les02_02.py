import requests
import time

url = "http://api.open-notify.org/iss-now.json"

while True:
    response = requests.get(url)
    data = response.json()

    lat = data["iss_position"]["latitude"]
    lon = data["iss_position"]["longitude"]

    print("Latitude:", lat, "| Longitude:", lon)

    time.sleep(5)