a = float(input("Inserisci la lunghezza di a: "))
b = float(input("\nInserisci la lunghezza di b: "))
h = float(input("\nInserisci l'altezza dalla base: "))

def calcolo_volume(a, b, h):
    return (a * b * h) / 3

volume = calcolo_volume(a, b, h)

peso_specifico = [4, 7, 10, 50, 210]

def calcolo_peso(peso_specifico, volume):
    pesi = []
    for p in peso_specifico:
        pesi.append(p * volume)
    return pesi

pesi = calcolo_peso(peso_specifico, volume)
pesi_specifici = list(map(calcolo_peso, pesi))


print(f"\nVolume del prisma triangolare: {volume:.2f} unità di volume")
print(f"\nPessi del prisma triangolare con differenti pesi specifici:")
for i, peso in enumerate(pesi):
    print(f"  - Peso specifico {peso_specifico[i]}: {peso:.2f} unità di peso")

#list(m)



