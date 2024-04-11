import os

dizionario_path = "dizionario.txt"
try:
    dizionario = set(open(dizionario_path, "r").read().split())
except FileNotFoundError:
    print(f"Errore: Il file '{dizionario_path}' non è stato trovato.")
    exit()
except Exception as e:
    print(f"Si è verificato un errore durante la lettura del file: {e}")
    exit()

def aggiungiParole(parola_aggiunta):

    # Controllo se la parola è già presente nel dizionario
    if parola_aggiunta in dizionario:
        print("La parola", parola_aggiunta, "è già presente nel dizionario.")
    else:
        # Aggiunta della parola al dizionario
        dizionario.add(parola_aggiunta)
        print("La parola", parola_aggiunta, "è stata aggiunta al dizionario.")


def correggiTesto(frase):

    # Suddivisione in parole
    parole = frase.split()

    # Correzione degli errori
    for i, parola in enumerate(parole):
        if parola not in dizionario:
            # Contrassegno la parola come errata
            parole[i] = f"[ERRORE] {parola}"

            # Suggerimenti di correzione
            suggerimenti = []
            for parola_corretta in dizionario:
                if len(parola) == len(parola_corretta):
                    distanza = sum(a != b for a, b in zip(parola, parola_corretta))
                    if distanza <= 1:
                        suggerimenti.append(parola_corretta)

            # Stampa dei suggerimenti
            if suggerimenti:
                print(f"Suggerimenti per '{parola}': {', '.join(suggerimenti)}")

    # Restituzione del testo corretto
    return " ".join(parole)

def main():
  
  while True:
    # Stampa del menu
    print("-" * 20)
    print("Menu")
    print("-" * 20)
    print("1. Aggiungi parola al dizionario")
    print("2. Correggi testo")
    print("3. Esci")
    print("-" * 20)

    # Scelta dell'utente
    scelta = input("Inserisci la tua scelta: ")

    # Gestione della scelta
    try:
      if scelta == "1":
        parola_aggiunta = input("Inserisci una parola da aggiungere al dizionario: ")
        aggiungiParole(parola_aggiunta)
      elif scelta == "2":
        frase = input("Inserisci una frase da correggere: ")
        testo_corretto = correggiTesto(frase)
        print("La frase inserita corretta è:  ",testo_corretto)
        
      elif scelta == "3":
        print("Arrivederci!")
        break
      else:
        print("Scelta non valida.")
    except Exception as e:
      print(f"Errore: {e}")

if __name__ == "__main__":
  main()
