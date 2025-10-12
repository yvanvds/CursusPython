🛈
Lesdoelen
Deze les helpt je om de basis goed onder de knie te krijgen voor we echte algoritmen gaan schrijven.
Je leert hoe je met lijsten werkt, hoe je door hun elementen loopt, en hoe je met condities en indices controle krijgt over wat er precies gebeurt.


📌 Deel 1: Lijsten en hun indexen

Een lijst (of array) is een verzameling waarden die je in één variabele kunt bewaren.

```python
getallen = [4, 7, 2, 9]
```

Elk element in een lijst heeft een index.
In Python begint tellen bij 0:
Index	Waarde
0	4
1	7
2	2
3	9

Je spreekt een element aan met lijstnaam[index].
print(getallen[0])   # toont 4
print(getallen[3])   # toont 9

Je kunt ook een element wijzigen:
getallen[2] = 10
print(getallen)  # [4, 7, 10, 9]

📝 Oefeningen

1. Dubbele waarden
Maak een lijst van 5 getallen. 
Gebruik indices om elk element te verdubbelen en toon daarna de nieuwe lijst.

2. Wisselen met index
Maak een lijst met 4 woorden.
Verwissel het tweede en vierde woord door hun index te gebruiken.

3. Maximum-element
Maak een lijst met 6 getallen.
Gebruik een variabele max en een for-lus om de grootste waarde te vinden.

4. Fibonacci reeks
Elk getal in een fibonacci reeks is de som van de twee vorige getallen. Vervang de vraagtekens door code die de reeks verder aanvult.

Fib = [0, 1]
for i in range(10):
    Fib.append(? + ?)
print(Fib)

📌 Deel 2: Lussen met range()
Met for ... in ... kun je over lijsten lopen.
Er zijn twee manieren:

1. Rechtstreeks over de waarden

for getal in getallen:
    print(getal)

2. Via de index

for i in range(len(getallen)):
    print("Index", i, ":", getallen[i])

De tweede manier is handig wanneer je de positie nodig hebt (bijv. om iets te wijzigen).

Je kan ook de meer complexe versie van range gebruiken. Daarin geef je de start, het einde en de stapgrootte mee aan range:

for i in range(2, len(getallen), 1):
    print(i, ":", getallen[i])

📝 Oefeningen

1. Som van oneven indexen
Maak een lijst van 10 getallen via numpy:
 
import numpy as np
getallen = np.arange(10)
 
Bereken de som van de elementen op oneven indexen (index 1, 3, 5, …).
Toon de som.

2. Nieuwe lijst maken

Gebruik een for-lus met range() om een nieuwe lijst te maken waarin elk getal verdubbeld is.

3. Omgekeerde volgorde

Toon de elementen van de lijst in omgekeerde volgorde.

4. Som van twee getallen

Doorloop de lijst en toon telkens de som van het huidige en het volgende getal.

📌 Deel 3: Condities combineren

Met if, elif en else kun je kiezen wat er gebeurt.

if x > 5:
    print("groter dan 5")
elif x == 5:
    print("gelijk aan 5")
else:
    print("kleiner dan 5")

Je kunt ook meerdere voorwaarden combineren:
Operator	Betekenis	Voorbeeld
and	én	if x > 5 and x < 10:
or	of	if x < 0 or x > 100:
not	niet	while not found:

📝 Oefeningen

1. Filteren
Maak een lijst met getallen van -5 tot 20.

getallen = np.random.randint(-5, 20, 10)

Toon enkel de getallen die groter zijn dan 10 én even.
(💡 Gebruik getal % 2 == 0 om te testen of iets even is.)

2. Selectie van namen
Maak een lijst met namen.
Toon enkel de namen die met een klinker beginnen of langer zijn dan 5 letters.

💡 Gebruik naam[0] in "AEIOUaeiou".

3. Temperatuurlijst
Maak een lijst met temperaturen in °C:

temperaturen = np.random.randint(-15, 40, 100)

Toon enkel de waarden die boven het vriespunt liggen én onder 30°C.
Toon daarnaast een teller voor het aantal dagen dat aan die voorwaarde voldoet.

Doorloop de lijst opnieuw en tel nu hoe vaak de outliers voorkomen (beneden het vriespunt en meer dan 30 gaden).

4. Scorecategorieën
Maak een lijst met scores tussen 0 en 100.

Tel voor elk van deze categorieën hoe vaak die voorkomt:
    • "geslaagd" als score ≥ 50
    • "onderscheiding" als score ≥ 75
    • "grootste onderscheiding" als score ≥ 90
    • "onvoldoende" anders
    
Gebruik if–elif–else.


📌 Deel 4: Geneste lussen

Een geneste lus betekent: een lus binnen een andere lus.
Dat is nuttig als je elk element met elk ander wilt vergelijken.

lijst = [3, 7, 1]
for i in range(len(lijst)):
    for j in range(len(lijst)):
        print(lijst[i], lijst[j])

Hierdoor worden alle mogelijke paren getoond.
Bijv. (3,3), (3,7), (3,1), (7,3), ...

📝 Oefeningen

1. Som deelbaar door 3
Maak een lijst met 10 willekeurige getallen.

Toon alle paren waarvan de som deelbaar is door 3.
Gebruik een geneste lus.

2. Dubbele waarden
Maak een lijst met getallen.

Toon alle paren (a, b) waarvoor a gelijk is aan b.
Gebruik for i in range(len(lijst)) en een geneste lus.

3. Vermenigvuldigingstabel
Toon met twee geneste lussen de tafels van vermenigvuldiging van 1 tot 10, netjes geformatteerd.

4. Gelijke sommen
Geef twee lijsten van getallen.
Zoek alle combinaties (x, y) waarbij x uit de eerste lijst en y uit de tweede komt, en waarbij x + y == 10.

📌 Deel 5: Wisselen van elementen
Soms wil je twee elementen van plaats verwisselen.
Dat kan niet met 

a = b
b = a

want dan verlies je de oorspronkelijke waarde van a.

De juiste manier:
temp = a
a = b
b = temp

of korter (maar in de meeste programmeertalen werkt dit niet):
a, b = b, a

Om in een lijst te wisselen:

getallen = [3, 8, 5]
i = 0
j = 2
getallen[i], getallen[j] = getallen[j], getallen[i]
print(getallen)  # [5, 8, 3]

📝 Oefeningen

1. Eerste en laatste
Schrijf een programma dat het eerste en laatste element van een lijst verwisselt.

2.  Minimum naar voren
Zoek de kleinste waarde in de lijst en wissel die met het eerste element.
Gebruik for en if.

3.Elementen sorteren (mini-versie)
Maak een lijst met 10 willekeurige getallen.

Gebruik een dubbele lus: telkens als twee opeenvolgende elementen fout staan (links > rechts), wissel ze.
Herhaal dit tot de lijst volledig gesorteerd is.

🎯 Samenvatting
Vaardigheid	Belangrijkste code
Lijst maken	lijst = [4, 7, 2]
Element tonen	print(lijst[i])
Element wijzigen	lijst[i] = nieuw_getal
Door indexen lopen	for i in range(len(lijst)):
Condities combineren	if x > 5 and x < 10:
Geneste lussen	for i in range(...): for j in range(...):
Wisselen	a, b = b, a
