#NUMERI PARI STAMPATI FILTRATI
def numero_pari(n):
    return n % 2 == 0
numeri = [1,2,3,4,5,6,7,8,9,10]

numeri_pari = list(filter(numero_pari, numeri))

print(numeri_pari)






def triplica(n):
    return n * 3
numeri_triplicati = list(map(triplica, numeri))
print(numeri_triplicati)