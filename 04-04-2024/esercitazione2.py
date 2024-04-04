#Quadrato numeri interi da uno a cinque
numeri_normali = [1,2,3,4,5]

def quadrato(n):
    return n * n
numeri_al_quadrato = list(map(quadrato, numeri_normali))
print("I numeri normali sono:",numeri_normali,"\n che al quadrato risulato essere:")
print(numeri_al_quadrato)
#crea un set contente i numeri interi da 1 a 5 ricavati da un range()


mio_set =  set(range(1,6))
print("Mio Set: ", mio_set)
#Verificare se l'elemento ananas è presente nella tupla

tupla = ("mela","banana","kiwi")
try:
    tupla.index("ananas")
    print("L'elemento ananas è presente nella tupla")
except ValueError:
    print("L'elemento ananas non è presente nella tupla")

