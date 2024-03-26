def prodotto_scalare(a, b):
    if len(a) != len(b):
        raise ValueError("I vettori devono avere la stessa lunghezza")
    prodotto = 0
    for i in range(len(a)):
        prodotto += a[i] * b[i]
    return prodotto

def prodotto_riga_per_colonna(a, b):
  """
  Calcola il prodotto riga per colonna tra due matrici.

  Args:
    a (list): La prima matrice.
    b (list): La seconda matrice.

  Returns:
    list: Una matrice che contiene il prodotto riga per colonna tra a e b.
  """
  if len(a[0]) != len(b):
    raise ValueError("Il numero di colonne della prima matrice deve essere uguale al numero di righe della seconda matrice")
  risultato = []
  for i in range(len(a)):
    riga = []
    for j in range(len(b[0])):
      prodotto = 0
      for k in range(len(a[0])):
        prodotto += a[i][k] * b[k][j]
      riga.append(prodotto)
    risultato.append(riga)
  return risultato


a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

prodotto_scalare = prodotto_scalare(a[0], b[0])
print("Prodotto scalare:", prodotto_scalare)
print("\n\\n\n\n\n\n\n\n")
prodotto_riga_colonna = prodotto_riga_per_colonna(a, b)
print("Prodotto riga per colonna:", prodotto_riga_colonna)



'''
def prodotto_scalare(v, w):
  if len(v) != len(w):
    raise ValueError("I vettori devono avere la stessa lunghezza")
  prodotto = 0
  for i in range(len(v)):
    prodotto += v[i] * w[i]
  return prodotto

v = [1,2,3,4]
w = [5,6,7,8]
prodotto_scalare = prodotto_scalare(v, w)
print("Prodotto scalare:", prodotto_scalare)

