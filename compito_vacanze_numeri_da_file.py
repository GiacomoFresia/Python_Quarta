# Un file contiene un numero intero per riga. Leggere il file e calcolare: somma, media,
# minimo e massimo.

def calcola():
    file = open("numeri.txt", "r", encoding='utf-8')
    righe = file.readlines()
    file.close()

    numeri = []
    for riga in righe:
        numeri.append(int(riga.strip()))

    somma = 0
    k = 0
    for n in numeri:
        somma = somma + n
        k = k + 1
    media = somma / k

    minimo = numeri[0]
    massimo = numeri[0]
    for n in numeri:
        if n > massimo:
            massimo = n
        elif n < minimo:
            minimo = n
    return somma, media, massimo, minimo

def main():
    s, m, massim, minim = calcola()
    print(f"Somma: {s}, Media: {m}, Minimo: {minim}, Massimo: {massim}")

    
    lista = ["2", "4", "7"]
    listaB = []
    for a in range(len(lista)):
        listaB.append(int(lista[a]))
    print(listaB)

if __name__=="__main__":
    main()