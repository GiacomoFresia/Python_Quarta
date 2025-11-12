# Scrivi un programma in Python che calcoli quanti sono i quadrati perfetti minori di 200.

import math             #dentro math c'è una funzione che fa la radice quadrata e una che fa la radice quadrata intera

contR = 0
for i in range (1, 200):
        radice = math.sqrt(i)                                               
        if(radice == int(radice)):
            print(f"La radice di {i} è un quadrato perfetto che vale: {radice}") 
            contR = contR + 1
        else:
            print(f"La radice di {i} non è un quadrato perfetto")
print(f"Numero di quadrati perfetti: {contR}")
