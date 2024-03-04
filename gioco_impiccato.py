import random 



def parola_casuale():
  parole = ["cane", "gatto", "casa", "albero", "fuoco", "mare", "cielo", "terra", "sole", "luna", "eccentricità", "secchio", "psicopatia","ellisse"]
  return random.choice(parole)

def nascondi_parola(parola):
  parola_nascosta = ""
  for lettera in parola:
    parola_nascosta += "*"
  return parola_nascosta


def gioco_impiccato():
  # Genera una parola casuale
  parola = parola_casuale()
  # Nasconde la parola con asterischi
  parola_nascosta = nascondi_parola(parola)
  # Imposta il numero di vite
  vite = 5
  # Ciclo di gioco
  while vite > 0 and parola_nascosta != parola:
    # Stampa la parola nascosta
    print(parola_nascosta)
    # Chiede una lettera all'utente
    lettera = input("Inserisci una lettera: ")
    # Controlla se la lettera è presente nella parola
    if lettera in parola:
      # Sostituisce gli asterischi con la lettera
      for i in range(len(parola)):
        if parola[i] == lettera:
          parola_nascosta = parola_nascosta[:i] + lettera + parola_nascosta[i+1:]
    else:
      # Rimuove una vita
      vite -= 1
      print("Lettera errata! Vite rimaste:", vite)
  # Stampa il risultato
  if vite > 0:
    print("Hai vinto! La parola era:", parola)
  else:
    print("Hai perso! La parola era:", parola)

def parola_casuale():
    parole = ["cane", "gatto", "casa", "albero", "fuoco", "mare", "cielo", "terra", "sole", "luna", "eccentricità", "secchio", "psicopatia", "ellisse"]
    return random.choice(parole)

def nascondi_parola(parola):
    parola_nascosta = ""
    for lettera in parola:
        parola_nascosta += "*"
    return parola_nascosta

def raddoppia_consonanti(stringa):
    nuova_stringa = ""
    vocali = "aàèéeiòoùu"

    for i, char in enumerate(stringa):
        if char in vocali:
            nuova_stringa += char
        else:
            nuova_stringa += char * 2
        if i == len(stringa) // 2:
            nuova_stringa += "o"
    return nuova_stringa

def gioco_impiccato_difficile():
    # Genera una parola casuale
    parola = parola_casuale()
    # Nasconde la parola con consonanti raddoppiate e 'o' nel mezzo
    parola_nascosta = raddoppia_consonanti(parola)
    # Imposta il numero di vite
    vite = 3
    # Lista di lettere già usate
    lettere_usate = []

    # Ciclo di gioco
    while vite > 0 and parola_nascosta != parola:
        # Stampa la parola nascosta
        print(parola_nascosta)
        # Chiede una lettera all'utente
        lettera = input("Inserisci una lettera: ")
        # Controlla se la lettera è già stata usata
        if lettera in lettere_usate:
            print("Lettera già usata!")
            continue
        # Aggiunge la lettera alle lettere usate
        lettere_usate.append(lettera)
        # Controlla se la lettera è presente nella parola
        if lettera in parola:
            # Sostituisce gli asterischi con la lettera
            for i in range(len(parola)):
                if parola[i] == lettera:
                    parola_nascosta = parola_nascosta[:i] + lettera + parola_nascosta[i+1:]
        else:
            # Rimuove una vita
            vite -= 1
            print("Lettera errata! Vite rimaste:", vite)

    # Stampa il risultato
    if vite > 0:
        print("Hai vinto! La parola era:", parola)
    else:
        print("Hai perso! La parola era:", parola)

    

print("\n Benvenuto nel gioco dell'impiccato! \n")
selezione = input("\n Iniziamo!! Seleziona 1 per gioco semplice, 2 per gioco difficile, 3 per uscire \n")

if selezione == "1":
  gioco_impiccato()
elif selezione == "2":
  gioco_impiccato_difficile()
elif selezione == "3":
  exit()






