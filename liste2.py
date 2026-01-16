# Gestione di una lista di numeri
# Data una lista di numeri interi, scrivere le funzioni richieste.

# Scrivere una funzione che, dato un numero k, restituisca una nuova lista contenente solo i numeri maggiori di k.
# Scrivere una funzione che conti quante volte compare un numero dato all’interno della lista.
# Scrivere una funzione che restituisca il valore minimo e il valore massimo della lista (senza usare min e max).
# Scrivere una funzione che restituisca una nuova lista con gli elementi in ordine inverso 
# (senza usare reverse o slicing).

def numeri_maggiori_di(numeri, k):
    lista_nuova = []
    for n in numeri:
        if n > k:
            lista_nuova.append(n)
    return lista_nuova

def conta(numeri, numero):
    n = 0
    for num in numeri:
        if num == numero:
            n = n + 1
    return n

def numeri_inversi(numeri):
    inversi = []
    for n in range(len(numeri) -1, -1, -1):
        inversi.append(numeri[n])
    return inversi

def unisci_liste(lista_a, lista_b):
    lista_finale = []
    for n in lista_a:
        lista_finale.append(n)
    for n in lista_b:
        if n in lista_finale:
            pass
        else:
            lista_finale.append(n)
    return lista_finale

def main():
    numeri = [10, 3, 7, 10, 5, 3, 8, 2, 7, 1]
    num = int(input("Inserisci il valore da confrontare: "))
    num_maggiori = numeri_maggiori_di(numeri, num)
    print(f"La lista con i valori maggiori di {num} è:\n{num_maggiori}")

    inversi = numeri_inversi(numeri)
    print(inversi)

    # Date due liste, restituire una nuova lista con gli elementi presenti in entrambe.
    lista_a = [1, 5, 8, 12, 15, 20]
    lista_b = [3, 5, 10, 12, 18, 20, 25]

    lista_f = unisci_liste(lista_a, lista_b)
    print(f"La lista finale è:\n{lista_f}")

if __name__=="__main__":
    main()