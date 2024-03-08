import requests
import json


def studenti_milano():
    """Ottiene e salva i dati sui laureati a Milano dal portale dati.comune.milano.it."""

    url = "https://dati.comune.milano.it/dataset/ds2714-laureati-negli-atenei-milanesi-anno-2021-suddivisi-per-genere"
    headers = {"Accept": "application/json"}  

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.content)

        with open("laureati_milano_2021.json", "w") as outfile:
            json.dump(data, outfile, indent=4)

        print("File JSON salvato correttamente.")
    else:
        print(f"Errore durante il recupero dei dati: {response.status_code}")

studenti_milano()
