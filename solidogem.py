from math import pi
from turtle import *

# Funzione per calcolare il volume di un cubo
def volume_cubo(lato):
  return lato**3

# Funzione per calcolare il volume di un parallelepipedo
def volume_paral(base, altezza):
  return base * altezza

# Funzione per calcolare il volume di una sfera
def volume_sfera(raggio):
  return (4/3) * pi * raggio**3

# Funzione per calcolare il volume di un cilindro
def volume_cilindro(raggio, altezza):
  return pi * raggio**2 * altezza

# Funzione per calcolare il peso di un solido
def peso_solido(volume, peso_specifico):
  return volume * peso_specifico


# Input dati solido
tipo_solido = input("Inserisci il tipo di solido (cubo, parallelepipedo, sfera, cilindro): ")
lato_cubo = float(input("Inserisci il lato del cubo (se cubo): "))
base_p = float(input("Inserisci la base del parallelepipedo (se parallelepipedo): "))
alte_p = float(input("Inserisci l'altezza del parallelepipedo (se parallelepipedo): "))
raggio_sfera = float(input("Inserisci il raggio della sfera (se sfera): "))
raggio_cilindro = float(input("Inserisci il raggio del cilindro (se cilindro): "))
altezza_cilindro = float(input("Inserisci l'altezza del cilindro (se cilindro): "))
peso_specifico = float(input("Inserisci il peso specifico del materiale: "))

# Calcolo volume
if tipo_solido == "cubo":
  volume = volume_cubo(lato_cubo)
elif tipo_solido == "parallepipedo":
  volume = volume_paral(base_p, alte_p)  
elif tipo_solido == "sfera":
  volume = volume_sfera(raggio_sfera)
elif tipo_solido == "cilindro":
  volume = volume_cilindro(raggio_cilindro, altezza_cilindro)

# Calcolo peso
peso = peso_solido(volume, peso_specifico)

# Stampa risultati
print("Volume:", volume + "m^3")
print("Peso:", peso + "Kg/m^3")



# Mantieni la finestra aperta
while True:
    update()