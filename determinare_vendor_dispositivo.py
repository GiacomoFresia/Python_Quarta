# chiede in input il mac address, apre il file, fa la ricerca riga per riga, 
# cerca i primi 3 byte se li trova ho trovato il vendor
# Determinare il vendor

def main():
    file = open(".\mac-vendors-export.csv", "r", encoding= 'utf-8')
    # encoding = 'utf-8' = risolve i probelmi dell'apertura del file su windows
    righe = file.readlines()
    file.close()
    #mac = input(f"Inserisci il tuo indirizzo MAC: ")
    mac = "C8:09:A8"
    for riga in righe:
        if riga[0:8] == mac:
            print(riga)
    #elemento1, elemento2 = righe[0::][0:2].split(",")
    #if righe[k][0:-1] == MAC_ADDRESS:
        #print(f"Il tuo {MAC_ADDRESS} coincide con {righe[k][0:-1]}")

if __name__ == "__main__":
    main()

