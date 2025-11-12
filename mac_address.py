def main():
    file = open(".\mac-vendors-export.csv", "r", encoding= 'utf-8')
    righe = file.readlines()
    file.close()

    mac_address = []
    vendor = []
    for riga in righe[1:10]:
        campi = riga.split(",") # Per ogni riga ho una lista di campi
        mac_address.append(campi[0])
        vendor.append(campi[1])

    mac = input("Inserisci il tuo mac address per intero: ").upper()
    for m, v in zip(mac_address, vendor):
        if m == mac[0:8]:
            print(f"Il produttore è {v}")

if __name__=="__main__":
    main()