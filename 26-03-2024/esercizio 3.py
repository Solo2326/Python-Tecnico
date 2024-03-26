#ciclo del menu

def sommapari():
  somma = 0
  for numero in range(2, 11, 2):
    somma += numero
  print("La somma dei primi 5 numeri pari è", somma)

def sommadispari(n):

  somma = 0
  numero = 1
  while numero <= n:
    somma += numero
    numero += 2
  return somma

def seriegeo(a, r, n):

  if r == 1:
    return a * n
  else:
    return a * (1 - r**n) / (1 - r)


def menu():
    print("\n Benvenuto nel menu'!\n")
selezione = input("\n Seleziona 1 per la funzione che stampa la somma dei primi numeri pari.\n\nSeleziona 2 per la funzione che stampa la somma dei n numeri dispari\n\nSeleziona 3 per la funzione che stampa la serie goniametrica di n numeri\n\nSeleziona 4 per uscire dal programma\n\n")
if selezione == "1":
        sommapari()
elif selezione == "2":
        sommadispari()
elif selezione == "3":
        seriegeo()
elif selezione == "4":
        exit()
else:
    print("Selezione non valida, riprova.")
menu()