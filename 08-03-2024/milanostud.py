import requests
import json


def studenti_milano():
    """Ottiene e salva i dati sui laureati a Milano dal portale dati.comune.milano.it."""

    url = "https://dati.comune.milano.it/dataset/c8cc2240-f6d2-4b8f-a230-1fb22a3ea190/resource/5b2ff8f3-2005-49d3-a8dd-6288a2327a1f/download/ds2714_laureati_negli_atenei_milanesi.json"
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