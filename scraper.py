import os
import csv
import json
import requests

# url CoinMarketCap API-ja za prenos podatkov o 1000 kriptovalutah
api_url = 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=1000'

# Imena map in datotek
data_directory = 'podatki'
# mapa, kamor bomo shranili datoteke
json_filename = 'kriptovalute.json'
# ime datoteke za surove podatke
csv_filename = 'kriptovalute.csv'
# ime datoteke za končne podatke



# Funkcije za delo z datotekami in spletnimi viri


def url_v_text(url):
    """Vsebino URL-ja vrne kot niz."""
    try:
        headers = {"User-Agent": "Edg/138.0.0.0"}
        vsebina = requests.get(url, headers=headers).text
        return vsebina
    except requests.exceptions.RequestException:
        print("Spletna stran ni dosegljiva")


def text_v_file(text, directory, filename):
    """Shrani besedilo v podano datoteko znotraj mape."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


def file_v_text(directory, filename):
    """Prebere vsebino datoteke in jo vrne kot niz."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()



# Funkcije za obdelavo API podatkov


def shrani_api(url, directory, filename):
    """Podatke iz API-ja shrani v .json datoteko."""
    text = url_v_text(url)
    if text:
        text_v_file(text, directory, filename)
    return text


def json_v_seznam_slovarjev(json_text):
    """Vrne seznam slovarjev kriptovalut iz JSON-a."""
    data = json.loads(json_text)
    return data.get('data', {}).get('cryptoCurrencyList', [])


def izlusci_iz_slovarja(slovar):
    """Iz enega slovarja izlušči pomembne podatke o valuti in ustvari nov lep slovar."""
    q = slovar.get('quotes', [{}])[0]
    
    return {
        'ime' : slovar.get('name'),
        'oznaka' : slovar.get('symbol'),
        'rang' : slovar.get('cmcRank'),
        'cena' : q.get('price'),
        'sprememba_1h' : q.get('percentChange1h'),
        'sprememba_24h' : q.get('percentChange24h'),
        'sprememba_7d' : q.get('percentChange7d'),
        'trzna_vrednost' : q.get('marketCap'),
        'obseg_24h' : q.get('volume24h'),
        'ponudba_v_obtoku' : slovar.get('circulatingSupply')
    }


def zapis_v_csv(fieldnames, rows, directory, filename):
    """Zapiše seznam slovarjev (vrstice) v CSV datoteko."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)



# Glavna funkcija


def main(redownload=True, reparse=True):
    """Izvede prenos, obdelavo in shranjevanje podatkov o kriptovalutah."""
    if redownload:
        shrani_api(api_url, data_directory, json_filename)

    if reparse:
        text = file_v_text(data_directory, json_filename)
        seznam = json_v_seznam_slovarjev(text)
        rows = [izlusci_iz_slovarja(slovar) for slovar in seznam]
        if rows:
            fieldnames = list(rows[0].keys())
            zapis_v_csv(fieldnames, rows, data_directory, csv_filename)



# Zagon programa


if __name__ == '__main__':
    main()