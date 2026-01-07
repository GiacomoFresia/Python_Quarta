# Dati due dizionari, crearne uno nuovo che contenga tutte le chiavi. Se una chiave è
# presente in entrambi, sommare i valori.

vendite_gennaio = {"mele": 120, "pere": 85, "arance": 200}
vendite_febbraio = {"mele": 95, "banane": 150, "arance": 180}

vendite_tot = {}

for prodotto in vendite_gennaio:
    vendite_tot[prodotto] = vendite_gennaio[prodotto]

for prodotto in vendite_febbraio:
    if prodotto in vendite_tot:
        vendite_tot[prodotto] = vendite_tot[prodotto] + vendite_febbraio[prodotto]
    else:
        vendite_tot[prodotto] = vendite_febbraio[prodotto]
    
print(vendite_tot)