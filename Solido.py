from math import pi
from turtle import *



# Funzione per calcolare il volume di un cubo
def volume_cubo(lato):
  return lato**3

# Funzione per calcolare il volume di una sfera
def volume_sfera(raggio):
  return (4/3) * pi * raggio**3

# Funzione per calcolare il volume di un cilindro
def volume_cilindro(raggio, altezza):
  return pi * raggio**2 * altezza

# Funzione per calcolare il peso di un solido
def peso_solido(volume, peso_specifico):
  return volume * peso_specifico

# Funzione per disegnare un cubo
def disegna_cubo(lato):
  t = turtle.Turtle()
  for i in range(4):
    t.forward(lato)
    t.left(90)
    t.forward(lato)
    t.left(90)
 

# Funzione per disegnare una sfera
def disegna_sfera(raggio):
  t = turtle.Turtle()
  t.up()
  t.setpos(0, -raggio)
  t.down()
  t.begin_fill()
  for i in range(360):
    t.forward(2 * raggio * pi / 360)
    t.left(1)
  t.end_fill()



# Funzione per disegnare un cilindro
def disegna_cilindro(raggio, altezza):
  t = turtle.Turtle()
  t.up()
  t.setpos(0, -altezza/2)
  t.down()
  t.begin_fill()
  for i in range(360):
    t.forward(2 * pi * raggio / 360)
    t.left(1)
  t.end_fill()
  t.up()
  t.setpos(0, altezza/2)
  t.down()
  t.begin_fill()
  for i in range(360):
    t.forward(2 * pi * raggio / 360)
    t.left(1)
  t.end_fill()
  t.up()
  t.setpos(raggio, 0)
  t.down()
  t.left(-90)
  t.forward(altezza)


# Esempio di utilizzo

# Input dati solido
tipo_solido = input("Inserisci il tipo di solido (cubo, sfera, cilindro): ")
lato_cubo = float(input("Inserisci il lato del cubo (se cubo): "))
raggio_sfera = float(input("Inserisci il raggio della sfera (se sfera): "))
raggio_cilindro = float(input("Inserisci il raggio del cilindro (se cilindro): "))
altezza_cilindro = float(input("Inserisci l'altezza del cilindro (se cilindro): "))
peso_specifico = float(input("Inserisci il peso specifico del materiale: "))

# Calcolo volume
if tipo_solido == "cubo":
  volume = volume_cubo(lato_cubo)
elif tipo_solido == "sfera":
  volume = volume_sfera(raggio_sfera)
elif tipo_solido == "cilindro":
  volume = volume_cilindro(raggio_cilindro, altezza_cilindro)

# Calcolo peso
peso = peso_solido(volume, peso_specifico)

# Stampa risultati
print("Volume:", volume)
print("Peso:", peso)

# Disegna solido
if tipo_solido == "cubo":
  disegna_cubo(lato_cubo)
elif tipo_solido == "sfera":
  disegna_sfera(raggio_sfera)
elif tipo_solido == "cilindro":
  disegna_cilindro(raggio_cilindro, altezza_cilindro)