# Leggere un file di testo e trovare la parola che compare più volte 
# (ignorando maiuscole/minuscole).

def trova_parola():
    file = open("articolo.txt", "r", encoding='utf-8')
    testo = file.read().lower()
    print("TESTO LETTO:")
    print(testo)
    file.close()
    d = {}
    parole = testo.split()
    for parola in parole:
        if parola in d:
            d[parola] = d[parola] + 1
        else:
            d[parola] = 1
    
    parola_max = ""
    n_max = 0
    for parola in d:
        if d[parola] > n_max:
            n_max = d[parola]
            parola_max = parola
    return parola_max, n_max

def main():
    max_parola, max_n = trova_parola()
    print(f"La parola più frequente è: {max_parola} con {max_n} volte")

if __name__=="__main__":
    main()