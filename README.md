# Analiza kriptovalut

V okviru predmeta **Uvod v programiranje** sem pripravil projektno nalogo, v kateri sem analiziral podatke o 1000 največjih kriptovalutah s strani [CoinMarketCap](https://coinmarketcap.com/) z uporabo programskega jezika Python.

## Pridobivanje in obdelava podatkov

Podatke sem s pomočjo glavne funkcije v datoteki **scraper.py** pridobil prek uradnega CoinMarketCap API-ja, jih shranil v .csv  in .json datoteko, ki sta dostopna v mapi **/podatki**.

## Analiza

V datoteki **analiza.ipynb** sem uvozil **kriptovalute.csv** in se poigral z raznimi metodami, kot so:
- **filtracija** in urejanje podatkov,
- **olepšava** tabele za bolšjo berljivost,
- ustvarjanje **vizualizacij** z raznimi grafičnimi prikazi,
- **primerjava** top kriptovalut po **ceni, tržni vrednosti in spremembah** v zadnjem dnevu,
- analiza **nihanja sprememb** top kriptovalut,
- analiza **razmerja** med obsegom trgovanja in tržno vrednostjo

## Ugotovitve

- Bitcoin je daleč najdražja kriptovaluta in tudi kar stabilna (ni hudega nihanja v spremembah cene),
- SOON je poceni kriptovaluta z veliko prometa v zadnjem dnevu, ki je kar zrasla v ceni v zadnjem tednu in nima prevelike tržne vrednosti, torej dober kandidat za investicijo
- največ kriptovalut ima tržno vrednost med 20M in 50M
- več kot 80% valut stane manj kot 1$
- nasploh so spremembe v zadnji uri stabilne (ni nihanj in ni hudih odstopanj), ko pa pogledamo spremembe v zadnjem dnevu in tednu pa vidimo nasploh pozitiven trend z večjimi nihanji in več odstopanji
- 48 Club Token je valuta, ki ima najvišje razmerje med obsegom trgovanja in tržno vrednostjo (13), torej se je ogromen delež tržne vrednosti obrnil v zadnjem dnevu (kupil/prodal)