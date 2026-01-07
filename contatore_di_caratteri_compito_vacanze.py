# Data una stringa, costruire un dizionario che associ a ogni carattere il numero di volte
# che compare.

testo = "abracadabra"
dizionario = {}

for carattere in testo:
    if carattere in dizionario:
        dizionario[carattere] = dizionario[carattere] + 1
    else:
        dizionario[carattere] = 1
print(dizionario)
