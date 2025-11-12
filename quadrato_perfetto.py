# Verificare se la somma dei primi n numeri dispari è un quadrato perfetto

import math    # Dentro math c'è una funzione che fa la radice quadrata e una che fa la radice quadrata intera

n = int(input("Inserisci un numero: "))
if n > 0:
    somma = 0
    for i in range(1, 2 * n + 1, 2):
        somma = somma + i
        radice_intera = math.isqrt(somma)    # Radice intera della somma
        print(f"La somma è {somma}, il quadrato perfetto: {radice_intera ** 2 == somma}") # Condizione nella stampa che restituisce sempre true