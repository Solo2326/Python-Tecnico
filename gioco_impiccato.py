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




    

print("\n Benvenuto nel gioco dell'impiccato!")
print("\n Iniziamo!!")
gioco_impiccato()
