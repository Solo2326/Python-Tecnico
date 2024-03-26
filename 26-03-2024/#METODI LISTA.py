#METODI LISTA

nuova_lista = ['alessio','jacopo','Claudio','marco','simone']
nuova_lista.append('nicola')
nuova_lista.insert(7,'Alberto')
bancatasx = ['alessandro','gabriele','riccardo','cristiano',]
bancatasx.pop(2)
nuova_lista.extend(bancatasx)
bancatasx.sort()
print(nuova_lista)


my_list = ['a','e','i','o','u',]

##   Metodi per le liste in Python

# append() - aggiunge un elemento alla fine della lista
my_list.append("nuovo_elemento")  

# clear() - rimuove tutti gli elementi dalla lista
my_list.clear()

# copy() - restituisce una copia della lista
new_list = my_list.copy() 

# count() - restituisce il numero di elementi con il valore specificato
num_occurrences = my_list.count("valore")

# extend() - aggiunge gli elementi di una lista (o di qualsiasi iterabile) alla fine della lista corrente
my_list.extend([1, 2, 3])  

# index() - restituisce l'indice del primo elemento con il valore specificato 
index_of_value = my_list.index("valore")  

# insert() - aggiunge un elemento alla posizione specificata
my_list.insert(2, "nuovo_elemento") 

# pop() - rimuove l'elemento alla posizione specificata (o l'ultimo se non specificato)
removed_item = my_list.pop(2)  

# remove() - rimuove il primo elemento con il valore specificato
my_list.remove("valore")  

# reverse() - inverte l'ordine degli elementi nella lista
my_list.reverse()

# sort() - ordina gli elementi della lista (crescente per default)
my_list.sort()  

