da_fare= ["Applicazione web","Applicazione android","Applicazione ios"]
stringfinale = (",".join(da_fare))
print(stringfinale.split(" "))

contatore = 0 
trovati = 0

for char in stringfinale:
    contatore += 1
    if char == ",":
        trovati += 1    

print(f"hai trovato {trovati} virgole nella lista ")