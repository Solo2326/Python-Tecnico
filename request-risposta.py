import requests

# API per i tassi di cambio
API_URL = "https://api.exchangerate-api.com/v4/latest/"

# Funzione per ottenere il tasso di cambio
def get_cambio(valuta_base, valuta_da_convertire):
    
    
    # Richiesta all'API
    response = requests.get(f"{API_URL}{valuta_base}")
    data = response.json()

    # Controllo del successo della richiesta
    if response.status_code != 200:
        raise RuntimeError(f"Errore API: {data['error']}")

    # Tasso di cambio
    cambio = data['rates'][valuta_da_convertire]

    return cambio

# Esempio di utilizzo
valuta_base = "EUR"
valuta_da_convertire = "USD"

cambio = get_cambio(valuta_base, valuta_da_convertire)

print(f"1 {valuta_base} equivale a {cambio} {valuta_da_convertire}")

