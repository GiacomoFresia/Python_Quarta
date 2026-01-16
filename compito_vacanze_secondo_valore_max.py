# Scrivere una funzione che trovi il secondo valore più grande in una lista di numeri (senza
# usare sort o sorted).

def secondo_valore_max(numeri):
    max1 = numeri[0]
    max2 = numeri[0]
    for n in numeri:
        if n > max1:
            max2 = max1
            max1 = n
        elif n > max2 and n != max1:
            max2 = n
    return max2

def main():
    valori = [45, 12, 78, 34, 67, 23, 89, 56]

    massimo2 = secondo_valore_max(valori)

    print(f"Il secondo valore massimo è: {massimo2}")

if __name__=="__main__":
    main()