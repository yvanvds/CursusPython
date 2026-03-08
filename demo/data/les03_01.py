import requests
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# ============================================================
# INSTELBARE PARAMETERS
# ============================================================

URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

MIN_MAGNITUDE = 0.0
# Zet op None om alle uren te tonen.
# Voorbeeld: 14 betekent enkel aardbevingen tussen 14:00 en 14:59 UTC.
FILTER_HOUR_UTC = None

# Schaling van de puntgrootte
SIZE_FACTOR = 18
MIN_POINT_SIZE = 12

# ============================================================
# DATA INLEZEN
# ============================================================

response = requests.get(URL, timeout=30)
response.raise_for_status()
data = response.json()

features = data["features"]

records = []
for feature in features:
    props = feature["properties"]
    coords = feature["geometry"]["coordinates"]

    mag = props.get("mag")
    time_ms = props.get("time")

    # Sommige records kunnen onvolledig zijn
    if mag is None or time_ms is None or coords is None or len(coords) < 2:
        continue

    records.append({
        "mag": mag,
        "time": pd.to_datetime(time_ms, unit="ms", utc=True),
        "longitude": coords[0],
        "latitude": coords[1],
        "depth_km": coords[2] if len(coords) > 2 else None,
        "place": props.get("place", "")
    })

df = pd.DataFrame(records)

# ============================================================
# FILTERS
# ============================================================

df = df[df["mag"] >= MIN_MAGNITUDE].copy()

if FILTER_HOUR_UTC is not None:
    df = df[df["time"].dt.hour == FILTER_HOUR_UTC].copy()

# ============================================================
# KLEUREN EN GROOTTES BEPALEN
# ============================================================

def magnitude_color(m):
    if m < 2:
        return "green"
    elif m < 4:
        return "orange"
    else:
        return "red"

df["color"] = df["mag"].apply(magnitude_color)

# Puntgrootte laten meegroeien met magnitude
# Negatieve magnitudes komen soms voor, dus eerst afkappen op 0
df["plot_size"] = df["mag"].clip(lower=0) * SIZE_FACTOR + MIN_POINT_SIZE

# ============================================================
# PLOT
# ============================================================

fig = plt.figure(figsize=(16, 8))
ax = plt.axes(projection=ccrs.PlateCarree())

# Wereldkaart met enkel kustlijnen
ax.set_global()
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.LAND)
ax.coastlines(linewidth=0.7)

# Geen landsgrenzen toevoegen, enkel kustlijnen

# Aardbevingen tekenen
ax.scatter(
    df["longitude"],
    df["latitude"],
    s=df["plot_size"],
    c=df["color"],
    alpha=0.75,
    transform=ccrs.PlateCarree()
)

# Titel opbouwen
title = f"Aardbevingen vandaag (USGS) - minimum magnitude {MIN_MAGNITUDE}"
if FILTER_HOUR_UTC is not None:
    title += f" - uur {FILTER_HOUR_UTC:02d}:00 tot {FILTER_HOUR_UTC:02d}:59 UTC"

plt.title(title)
plt.tight_layout()
plt.show()