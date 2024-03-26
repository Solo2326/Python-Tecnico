#LA MIA FUNZIONE INIZIALE
def prodotto_scalare(v, w):
  if len(v) != len(w):
    raise ValueError("I vettori devono avere la stessa lunghezza")
  prodotto = 0
  for i in range(len(v)):
    prodotto += v[i] * w[i]
  return prodotto

v = []
for i in range(int(input("Inserisci la dimensione del primo vettore: "))):
  v.append(int(input("Inserisci l'elemento {} del primo vettore: ".format(i + 1))))
w = []
for i in range(int(input("Inserisci la dimensione del secondo vettore: "))):
  w.append(int(input("Inserisci l'elemento {} del secondo vettore: ".format(i + 1))))


prodotto_scalare = prodotto_scalare(v, w)
print("Prodotto scalare:", prodotto_scalare)





