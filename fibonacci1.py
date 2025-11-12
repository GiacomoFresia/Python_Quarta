n = int(input("Quanti numeri di Fibonacci vuoi: "))
a, b = 1, 1  # Inizializzazione NON dichiarazione!!!      # pass Non fa niente, è un instruzione vuota
             #pass = istruzione che rende il codice corretto e quindi eseguibile se non ci sono altre istruzioni al suo interno
if n > 2:
    for i in range(n):
        print(a, end = " - ")
        a,b = b,a+b
elif n == 0:
     print(f"Nessun valore")
elif n == 2:
    print(a, end = " - ")
    print(b)
elif n == 1:
    print("Hai inserito un solo numero")