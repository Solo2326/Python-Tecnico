import os

def distanza_levenshtein(parola1, parola2):
 
  m = len(parola1)
  n = len(parola2)
  dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

  for i in range(m + 1):
    for j in range(n + 1):
      if i == 0:
        dp[i][j] = j
      elif j == 0:
        dp[i][j] = i
      elif parola1[i - 1] == parola2[j - 1]:
        dp[i][j] = dp[i - 1][j - 1]
      else:
        dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)

  return dp[m][n]

def correggiTesto(frase, dizionario):

  parole = frase.split()
  correzioni = []

  for parola in parole:
    if parola not in dizionario:
      min_distanza = float('inf')
      corretta = parola
      for parola_corretta in dizionario:
        distanza = distanza_levenshtein(parola, parola_corretta)
        if distanza < min_distanza:
          min_distanza = distanza
          corretta = parola_corretta

      correzioni.append(corretta)
    else:
      correzioni.append(parola)

  return " ".join(correzioni)

def main():
  dizionario_path = "C:\Users\bebof\Desktop\Git-Hub\Python-Tecnico\08-04-2024\dizionario.txt"
  try:
    dizionario = set(open(dizionario_path, "r").read().split())
  except FileNotFoundError:
    print(f"Errore: Il file '{dizionario_path}' non è stato trovato.")
    exit()
  except Exception as e:
    print(f"Si è verificato un errore durante la lettura del file: {e}")
    exit()

  while True:
    # Stampa del menu
    print("-" * 20)
    print("Menu")
    print("-" * 20)
    print("1. Correggi testo")
    print("2. Esci")
    print("-" * 20)

    # Scelta dell'utente
    scelta = input("Inserisci la tua scelta: ")

    # Gestione della scelta
    try:
      if scelta == "1":
        frase = input("Inserisci una frase da correggere: ")
        testo_corretto = correggiTesto(frase, dizionario)
        print("La frase corretta è:", testo_corretto)
      elif scelta == "2":
        print("Arrivederci!")
        break
      else:
        print("Scelta non valida.")
    except Exception as e:
      print(f"Errore: {e}")

if __name__ == "__main__":
  main()
