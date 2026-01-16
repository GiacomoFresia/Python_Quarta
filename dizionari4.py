# Data una stringa, costruire un dizionario che associ a ogni carattere il numero di volte che compare.

# Dato un dizionario che associa nomi di studenti ai loro voti (un voto per studente),
# trovare quale voto compare più spesso.

# Dati due dizionari, crearne uno nuovo che contenga tutte le chiavi. Se una chiave è
# presente in entrambi, sommare i valori.

def conta(stringa):
    d = {}
    for c in stringa:
        if c in d:
            d[c] = d[c] + 1
        else:
            d[c] = 1
    return d

def voto_piu_frequente(voti):
    d = {}
    for voto in voti:
        v = voti[voto]
        if v in d:
            d[v] = d[v] + 1
        else:
            d[v] = 1
    freq_max = 0
    for voto in d:
        if d[voto] > freq_max:
            freq_max = d[voto]
            voto_max = voto
    return voto_max
        
def crea_dizionario(vendite_gennaio, vendite_febbraio):
    vendite_tot = {}
    for v in vendite_gennaio:
        vendite_tot[v] = vendite_gennaio[v]
    for v in vendite_febbraio:
        if v in vendite_tot:
            vendite_tot[v] = vendite_tot[v] + vendite_febbraio[v]
        else:
            vendite_tot[v] = vendite_febbraio[v]
    return vendite_tot

def main():
    testo = "abracadabra"
    diz = conta(testo)
    print(diz)


    studenti_voti = {
    "Marco": 7,
    "Sara": 8,
    "Luca": 6,
    "Elena": 8,
    "Paolo": 7,
    "Giulia": 8,
    "Andrea": 6,
    "Chiara": 7
    }
    voto_max = voto_piu_frequente(studenti_voti)
    print(f"Il voto piu frequente è: {voto_max}")


    vendite_gennaio = {"mele": 120, "pere": 85, "arance": 200}
    vendite_febbraio = {"mele": 95, "banane": 150, "arance": 180}
    vendite_tot = crea_dizionario(vendite_gennaio, vendite_febbraio)
    print(f"Il nuovo dizionario è:\n{vendite_tot}")

if __name__=="__main__":
    main()