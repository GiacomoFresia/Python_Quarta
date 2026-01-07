# Data una lista di interi, scrivere una funzione che restituisca due liste separate: una con
# i numeri pari e una con i dispari.

def pari_dispari(numeri):
    pari = []
    dispari = []
    for n in numeri:
        if n % 2 == 0:
            pari.append(n)
        else:
            dispari.append(n)
    return pari, dispari

def main():
    numeri = [3, 8, 12, 7, 2, 15, 20, 9, 4]

    pari, dispari = pari_dispari(numeri)

    print(f"La lista con i numeri pari è: {pari}")
    print(f"La lista con i numeri dispari è: {dispari}")

if __name__=="__main__":
    main()
