import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# INSTELBARE VARIABELEN
# Pas deze waarden aan als je andere groepen wilt vergelijken.
# ============================================================
ENTITIES = [
    "High-income countries",
    "Upper-middle-income countries",
    "Lower-middle-income countries",
    "Low-income countries"
]



CSV_FILE = "immigrants-to-belgium-where-did-they-move-from.csv"

# Zet hier de naam van de kolom met de aantallen immigranten.
# Controleer eventueel eerst met: print(df.columns)
VALUE_COLUMN = "Immigrants to Belgium: Where did they move from?"


# ============================================================
# 1. DATA INLEZEN
# We lezen het csv-bestand in met pandas.
# ============================================================
df = pd.read_csv(CSV_FILE)

# Toon de kolomnamen zodat je kan controleren of VALUE_COLUMN klopt.
print("Kolommen in de dataset:")
print(df.columns.tolist())
print()


# ============================================================
# 2. BELANGRIJKE KOLOMMEN CONTROLEREN
# We stoppen met een duidelijke foutmelding als een kolom ontbreekt.
# ============================================================
required_columns = ["Entity", "Year", VALUE_COLUMN]

for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"Kolom niet gevonden: {col}")


# ============================================================
# 3. WAARDEKOLOM OMZETTEN NAAR GETALLEN
# Soms leest pandas getallen in als tekst.
# Met to_numeric zetten we die om naar echte numerieke waarden.
# Waarden die niet omgezet kunnen worden, worden NaN.
# ============================================================
df[VALUE_COLUMN] = pd.to_numeric(df[VALUE_COLUMN], errors="coerce")

# Ook Year zetten we voor de zekerheid om naar getallen.
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")


# ============================================================
# 4. RIJEN MET ONTBREKENDE JAAR- OF WAARDEGEGEVENS VERWIJDEREN
# Deze rijen kunnen we niet gebruiken in de grafiek.
# ============================================================
df = df.dropna(subset=["Year", VALUE_COLUMN])

# Year terug omzetten naar gehele getallen voor nette labels.
df["Year"] = df["Year"].astype(int)


# ============================================================
# 5. ENKEL DE GEWENSTE ENTITIES SELECTEREN
# ============================================================
df_filtered = df[df["Entity"].isin(ENTITIES)].copy()


# ============================================================
# 6. CONTROLEREN OF ALLE ENTITIES GEVONDEN ZIJN
# ============================================================
gevonden_entities = set(df_filtered["Entity"].unique())
gevraagde_entities = set(ENTITIES)
ontbrekende_entities = gevraagde_entities - gevonden_entities

if ontbrekende_entities:
    print("Waarschuwing: deze entities werden niet gevonden:")
    for entity in sorted(ontbrekende_entities):
        print("-", entity)
    print()


# ============================================================
# 7. DATA OMVORMEN NAAR BREDE TABEL
# Elke rij wordt een jaar, elke kolom een entity.
# ============================================================
pivot_df = df_filtered.pivot(index="Year", columns="Entity", values=VALUE_COLUMN)


# ============================================================
# 8. KOLOMMEN IN DE GEWENSTE VOLGORDE ZETTEN
# ============================================================
beschikbare_entities = [entity for entity in ENTITIES if entity in pivot_df.columns]
pivot_df = pivot_df[beschikbare_entities]


# ============================================================
# 9. ONTBREKENDE WAARDEN OPVULLEN MET 0
# ============================================================
pivot_df = pivot_df.fillna(0)


# ============================================================
# 10. CONTROLEREN OF ER EFFECTIEF NUMERIEKE DATA IS
# Dit helpt om sneller te begrijpen wat er fout loopt.
# ============================================================
print("Eerste rijen van de pivot-tabel:")
print(pivot_df.head())
print()
print("Datatypes van de pivot-tabel:")
print(pivot_df.dtypes)
print()


# ============================================================
# 11. STACKED BAR GRAFIEK MAKEN
# ============================================================
ax = pivot_df.plot(
    kind="bar",
    stacked=True,
    figsize=(12, 6),
    width=0.8
)

ax.set_title("Immigratie naar België per herkomstgroep")
ax.set_xlabel("Jaar")
ax.set_ylabel("Aantal immigranten")

plt.xticks(rotation=45)
plt.legend(title="Entity")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()