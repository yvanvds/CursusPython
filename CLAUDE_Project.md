# Claude Project: Cursus Python (6EWI / 6WEWI)

Dit document beschrijft de context van de cursus zodat Claude consistent nieuwe
hoofdstukken kan schrijven die aansluiten bij wat er al gezien is.

---

## 1. Over de cursus

**Titel:** Cursus Python
**Doelpubliek:** Leerlingen 6de jaar EWI / WEWI (17–18 jaar, wiskunde/wetenschap-richting) in België.
**Auteur:** Yvan Vander Sanden
**Repo:** https://github.com/yvanvds/CursusPython
**Formaat:** Jupyter Book (`.ipynb`-bestanden onder `book/moduleNN/`), gebouwd
met de TeachBooks-stack (Sphinx + jupyter-book + thebe voor live code).

**Niveau:** Beginner → midden gevorderd. Geen voorkennis programmeren, wél
wiskundige rijpheid (afgeleiden, integralen, trigonometrie, exponentiële
functies worden zonder aarzelen gebruikt).

---

## 2. Pedagogische aanpak en toon

Belangrijk: ELK nieuw hoofdstuk moet deze stijl respecteren.

- **Nederlandstalig**, vlot en directe aanspreking ("we gaan...", "probeer eens...").
- **Probleemgestuurd**: vertrek van een concrete vraag of fenomeen, niet van syntax.
- **Real-world context**: aardbevingen, ISS-positie, klimaatdata, geluid,
  trillingen — geen "foo/bar"-voorbeelden.
- **Wiskunde en fysica zijn de motivatie**, programmeren is het werktuig.
- **Exploratief**: "voer dit uit, kijk wat er gebeurt, pas aan". Veel kleine
  oefeningen tussen de uitleg.
- **Foutgericht**: tonen wat misgaat hoort er bij, niet enkel het juiste antwoord.
- **Korte cellen**: liefst veel kleine code-cellen met telkens uitleg in
  markdown-cellen ertussen, geen muren tekst of code.
- **Visualisatie waar het kan** (`matplotlib`, `turtle`).
- **Wiskunde in LaTeX** (`$...$` of `$$...$$`) — MyST/dollarmath staat aan.

---

## 3. Bestandsstructuur en conventies

- Lesbestanden: `book/moduleNN/les_XX_naam.ipynb`
- Toevoegen aan `book/_toc.yml` onder de juiste module.
- Een lesnotebook begint met een `# Titel`-cel en daarna afwisselend
  markdown- en code-cellen.
- Oefeningen mogen in `demo/` of `demo/data/` staan als losse `.py`-scripts
  die in de tekst aangehaald worden.
- Datasets in `book/moduleXX/` of in een aparte data-map naast het notebook.
- Bestandsnamen in snake_case, lowercase, ASCII (geen accenten).

---

## 4. Wat is al behandeld? (samenvatting per module)

Claude moet hier rekening mee houden: **niet opnieuw uitleggen wat hier
genoemd wordt**, tenzij de leerling expliciet vraagt om herhaling. Wél mag je
ernaar verwijzen ("zoals we in module 2 bij lijsten gezien hebben...").

### Module 1 — Basisprincipes Programmeren

| Les | Inhoud |
|-----|--------|
| 01 intro | Wat is programmeren, algoritmisch denken, pseudocode, eerste `print()`/`input()`, `import math`, `math.pi`. |
| 02 variabelen | Variabelen, datatypes (`int`, `float`, `str`), casting (`int()`, `float()`, `str()`), `type()`, rekenkundige operatoren, modulo, geheeltallige deling. Toepassingen: BMI, °C↔°F, wisselgeld. |
| 03 condities | `if/elif/else`, vergelijkingsoperatoren, `for ... in range()`, `while`, `random.randint()`. Toepassingen: getal raden, pariteit, cijfers tellen. |

### Module 2 — Eenvoudige Datastructuren

| Les | Inhoud |
|-----|--------|
| 01 lijsten | `list`, `tuple`, indexering (0-based), `len/min/max/sum`, `.append`/`.remove`, intro `numpy` met `np.array`, `np.linspace`, `np.arange`, vectoroperaties. |
| 02 lijsten gebruiken | `range(len(...))`, geneste lussen, logische operatoren (`and`/`or`/`not`), tuple-unpacking voor swap. Fibonacci, filteren. |
| 03 sorteren | Bubble sort en insertion sort *zelf schrijven*, vergelijken met ingebouwde `.sort()`, `time.time()` voor timing, intro Big-O als concept. |
| 04 turtle | `turtle.Turtle`, `forward/left/penup/pendown/color`, recursie (fractalboom, Koch, Sierpinski), random kleuren. |

### Module 3 — Wiskundige probleemoplossing

| Les | Inhoud |
|-----|--------|
| 01 functies | `def`, parameters, `return`, scope, functies als herbruikbare blokken. |
| 02 bisectie | Numeriek nulpunten zoeken via interval-halvering, plotten met `matplotlib.pyplot`, "voldoende nauwkeurig" vs. exact. |
| 03 functies (verdieping) | Eigen `.py`-modules met functies, audio als context: `numpy` voor signalen, `sounddevice` voor afspelen, sinussen, amplitude, mengen, fade-envelopes, MIDI→frequentie. |
| 04 integralen | Riemann-sommen, trapeziumregel, `numpy.trapezoid`, `scipy.integrate.quad`, vlak onder grafiek invullen met matplotlib. |

### Module 4 — Data-analyse en visualisatie

| Les | Inhoud |
|-----|--------|
| 01 klimaatdata | CSV inlezen met `pandas`, `.head()`, `.shape`, `.mean()`, `.info()`, boolean masking, kolomselectie, rolling average, plotten van temperatuuranomalieën (NH vs ZH). |
| 02 json | `requests.get(...).json()`, nested dicts/lists, ISS-positie, aardbevingsdata, wereldkaart-visualisatie (cartopy optioneel), tijdstempels. |
| 03 ai | AI als code-assistent (Claude/ChatGPT), prompt engineering, kritisch evalueren van gegenereerde code, workflow: probleem → data inspecteren → gerichte vraag → verifiëren. |

### Module 5 — Golven en trillingen

| Les | Inhoud |
|-----|--------|
| 01 trillingen | Discreet sampelen (samplerate), sinussignaal $\sin(2\pi f t)$, amplitude, frequentie, lineaire en exponentiële demping, superpositie, gepluk-snaar als gedempte trilling, hoorbaar maken via `sounddevice`. |

---

## 5. Bibliotheken die al geïntroduceerd zijn

Claude mag deze gebruiken zonder ze opnieuw "from scratch" uit te leggen:

`math`, `random`, `time`, `numpy`, `matplotlib.pyplot`, `turtle`,
`pandas`, `requests`, `scipy.integrate`, `sounddevice`, `cartopy` (optioneel).

Niet (of nauwelijks) gezien — eerste gebruik vereist korte intro:
OOP/`class`, decorators, generators, `async`/`await`, type hints, `pytest`,
file I/O met `open()` voorbij eenvoudige CSV, regex, web scraping,
machine learning frameworks.

---

## 6. Concepten die al gekend zijn

- Variabelen, primitieve types, casting
- `if/elif/else`, `for` met `range`, `while`, geneste lussen
- Lijsten, tuples, indexering, NumPy-arrays
- Functies (`def`, parameters, return), recursie
- Eigen `.py`-modules importeren
- Plotten met matplotlib (lijn, scatter, vulling)
- DataFrames basis (filteren, statistieken, plotten)
- HTTP GET en JSON parsen
- Numerieke methoden (bisectie, trapezium)
- Signaalgeneratie (sinus, demping, superpositie)

Niet uitgelegd — wel introduceren als je het gebruikt:
list comprehensions (worden spaarzaam gebruikt), dictionaries als first-class
datastructuur (oppervlakkig gezien via JSON), exception handling
(`try/except`), klassen, bestand-IO buiten pandas.

---

## 7. Hoe vraag je een nieuw hoofdstuk?

Wanneer ik vraag "schrijf een nieuw hoofdstuk over X", doe dan dit:

1. **Bepaal in welke module het past** (en stel een lesnummer voor) op basis
   van de inhoudstabel hierboven. Vraag bevestiging als het twijfelachtig is.
2. **Bouw expliciet voort op wat al gekend is** uit de modules ervoor.
   Hergebruik notatie en stijl (sinusvoorbeelden, plotting-conventies, etc.).
3. **Lever het hoofdstuk als één Jupyter notebook** (`.ipynb`-JSON of
   markdown-equivalent in MyST), met:
   - korte motiverende intro (probleemstelling/context)
   - afwisselend uitleg en kleine code-cellen
   - visualisaties waar zinvol
   - een paar oefeningen op het einde (oplopende moeilijkheid)
4. **Geef ook de regel die in `book/_toc.yml` toegevoegd moet worden**.
5. **Wiskunde in LaTeX**, code in Python 3, alle uitleg in het Nederlands.
6. **Niet overdrijven met theorie**: een leerling moet om de paar minuten zelf
   iets uit te voeren krijgen.

Vermijd:
- Engelstalige uitleg of variabelennamen die de uitleg verstoren
  (variabelen mogen Engels zijn, comments en tekst niet).
- Een hele bibliotheek-API droog opsommen.
- Refereren aan onderwerpen die nog niet aan bod kwamen zonder ze even kort te
  introduceren.
- "Hello World"-stijl voorbeelden zonder context.

---

## 8. Snelle checklist bij het reviewen van een nieuw hoofdstuk

- [ ] Past in de progressie van de bestaande module?
- [ ] Bouwt voort op concepten uit eerdere modules zonder onnodige herhaling?
- [ ] Gebruikt enkel libraries die al geïntroduceerd zijn (of introduceert
      nieuwe expliciet)?
- [ ] Bevat een concrete real-world of wiskundige toepassing?
- [ ] Korte cellen, veel afwisseling, oefeningen op het eind?
- [ ] Nederlandstalig, vlot, persoonlijk, geen academische droogheid?
- [ ] LaTeX voor wiskunde, plots waar nuttig?
