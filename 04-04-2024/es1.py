#ESERCITAZIONE 04-04-24

#Parte 1
stringa = "ciao mondo"
nuova_stringa= stringa.upper()
print(nuova_stringa) 

#parte 2
ultimi_5 = stringa[-5:].upper().replace("o", "k")
print(ultimi_5)

#parte 3

nome = input("Inserisci un nome")
cognome = input("Inserisci un cognome")
frase = (f"Il mio nome è {nome} ed il cognome è {cognome}")
print(frase)
