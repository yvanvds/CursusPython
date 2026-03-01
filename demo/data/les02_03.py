import requests

# de URL van de afbeelding die we willen downloaden
img_url = "https://svs.gsfc.nasa.gov/vis/a000000/a002900/a002915/bluemarble-2048.png"
# het pad waar we de afbeelding willen opslaan
img_path = "world.png"

# download de afbeelding
r = requests.get(img_url)
# controleer of de download succesvol was
r.raise_for_status()

# schrijf de afbeelding naar een bestand
with open(img_path, "wb") as f:
    f.write(r.content)

print("Gedownload:", img_path)