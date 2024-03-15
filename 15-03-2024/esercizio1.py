import requests
#Funzione che effettua la conversione da binario a decimale utilizzando l'API.
def binario_a_deci(num_bin):
  try:
    # Conversione tramite API
    risposta = requests.get(f"https://networkcalc.com/api/binary/{num_bin}")
    if risposta.status_code == 200:
      data = risposta.json()
      if 'converted' in data:
        return data['converted']
  except requests.exceptions.ConnectionError:
    print("**ATTENZIONE: Connessione API non disponibile. Conversione manuale in corso...**")
  
# Conversione manuale
  return converti_binario_decimale_manuale(num_bin)

#Funzione che effettua manualmente la conversione se l'API non funziona
def converti_binario_decimale_manuale(num_bin):
  valore_esadecimale = "0123456789ABCDEF"
  lunghezza_binario = len(num_bin)
  valore_decimale = 0
  potenza_due = 1
  for i in range(lunghezza_binario-1, -1, -1):
    valore_decimale += int(num_bin[i]) * potenza_due
    potenza_due *= 2
  indice_esadecimale = valore_decimale % 16
  quoziente = valore_decimale // 16
  numero_esadecimale = valore_esadecimale[indice_esadecimale]
  while quoziente > 0:
    indice_esadecimale = quoziente % 16
    quoziente //= 16
    numero_esadecimale = valore_esadecimale[indice_esadecimale] + numero_esadecimale
  return numero_esadecimale

#Funzione che conta gli zeri e uno del numero binario
def conta_zeri_uno(binary_num):
    num_zero = binary_num.count('0')
    num_uno = binary_num.count('1')
    print("Numero di 0 nel numero binario:", num_zero)
    print("Numero di 1 nel numero binario:", num_uno)
#Funzione main dove si richiede l'input e svolge le funzioni
def main():
    num_bin = input("Inserisci un numero binario: ")
    result = binario_a_deci(num_bin)
    print("Decimale (manuale):", result)
    conta_zeri_uno(num_bin)
    
#Fa partire il programma
main()