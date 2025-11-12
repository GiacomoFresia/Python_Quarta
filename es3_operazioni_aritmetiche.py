# Scrivi un programma che permetta all'utente di effettuare le quattro operazioni aritmetiche. 
# Per prima cosa chiede all'utente quale operazione desidera eseguire 
# (0: somma, 1: sottrazione, 2: moltiplicazione: 3 divisione), poi chiede all'utente 
# due numeri e stampa il risultato dell'operazione.

n = int(input("Inserisci l'operazione che vuoi: 0:somma, 1:sottrazione, 2:moltiplicazione:, 3:divisione: "))
n1 = int(input("Dammi 1 numero: "))
n2 = int(input("Dammi 1 numero: "))

if n == 0:
    somma = n1 + n2
    print(somma)
elif n == 1:
    sottrazione = n1 - n2
    print(sottrazione)
elif n == 2:
    moltiplicazione = n1 * n2
    print(moltiplicazione)
elif n == 3:
    divisione = n1 / n2
    print(divisione)
else:
    print("Input non valido")
