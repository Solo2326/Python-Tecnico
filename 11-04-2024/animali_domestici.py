animali_domestici = {}

while True:
    nome_animale = input("Inserisci il nome dell'animale: ")
    specie = input("Inserisci la specie: ")
    razza = input("Inserisci la razza: ")
    eta = int(input("Inserisci l'età: "))
    nome_proprietario = input("Inserisci il nome del proprietario: ")

    animali_domestici[nome_animale] = {
        "specie": specie,
        "razza": razza,
        "eta": eta,
        "proprietario": nome_proprietario
    }

    cont = input("Vuoi inserire un altro animale? (s/n): ")
    if cont.lower() == "n":
        break

print(animali_domestici)
