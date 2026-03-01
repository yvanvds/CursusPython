import requests

url = "http://api.open-notify.org/astros.json"
response = requests.get(url)

data = response.json()
number = data['number']

print("Er zijn momenteel " + str(number) + " mensen in de ruimte.")

for person in data['people']:
    # toon nu de naam van elke persoon
    print("??")