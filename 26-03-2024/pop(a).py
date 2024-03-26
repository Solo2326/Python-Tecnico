lista = ["a", "b", "c", "a"]
print(f"Lista originale: {lista}")

def togli_a(lista):
  
  while "a" in lista:
    lista.pop(lista.index("a"))

  return lista

# Esempio di utilizzo

nuova_lista = togli_a(lista)


print(f"Nuova lista: {nuova_lista}")
