#LA MIA FUNZIONE INIZIALE
def prodotto_scalare(v, w):
  if len(v) != len(w):
    raise ValueError("I vettori devono avere la stessa lunghezza")
  prodotto = 0
  for i in range(len(v)):
    prodotto += v[i] * w[i]
  return prodotto
#somma
def somma(v, w):
  if len(v) != len(w):
    raise ValueError("I vettori devono avere la stessa lunghezza")
  somma = []
  for i in range(len(v)):
    somma.append(v[i] + w[i])
  return somma
#differenza
def differenza(v, w):
  if len(v) != len(w):
    raise ValueError("I vettori devono avere la stessa lunghezza")
  differenza = []
  for i in range(len(v)):
    differenza.append(v[i] - w[i])
  return differenza




v = []
for i in range(int(input("Inserisci la dimensione del primo vettore: "))):
  v.append(int(input("Inserisci l'elemento {} del primo vettore: ".format(i + 1))))
w = []
for i in range(int(input("Inserisci la dimensione del secondo vettore: "))):
  w.append(int(input("Inserisci l'elemento {} del secondo vettore: ".format(i + 1))))



somma_scalare = somma(v, w)
differenza_scalare = differenza(v, w)
prodotto_scalare = prodotto_scalare(v, w)
print("Somma dei vettori:", somma_scalare)
print("Differenza dei vettori:", differenza_scalare)
print("Prodotto scalare:", prodotto_scalare)





