# Un dizionario associa nomi di squadre a liste di giocatori. Scrivere funzioni per: (a)
# trovare la squadra con più giocatori, (b) verificare se un giocatore è in una squadra, (c)
# trasferire un giocatore da una squadra all’altra.

def squadra_piu_giocatori(squadre):
    squadra_max = ""
    n_max = 0
    for squadra in squadre:
        if len(squadre[squadra]) > n_max:
            n_max = len(squadre[squadra])
            squadra_max = squadra
    return squadra_max, n_max

def verifica_giocatore_in_squadra(squadre, giocatoreX):
    squadraX = ""
    for squadra in squadre:
        if giocatoreX in squadre[squadra]:
            squadraX = squadra
    return squadraX

def trasferire(squadre, giocatoreX, nuovaSquadra):
    for squadra in squadre:
        if giocatoreX in squadre[squadra] and nuovaSquadra in squadre:
            squadre[squadra].remove(giocatoreX)
            squadre[nuovaSquadra].append(giocatoreX)
    print(squadre)

def main():
    squadre = {
    "Juventus": ["Vlahovic", "Chiesa", "Locatelli", "Bremer"],
    "Inter": ["Lautaro", "Thuram", "Barella", "Bastoni", "Calhanoglu"],
    "Milan": ["Leao", "Theo", "Reijnders"]
    }

    squadra_max, num_max = squadra_piu_giocatori(squadre)
    print(f"La squadra con più giocatori è {squadra_max} con {num_max} giocatori")

    giocatoreX = input("Inserisci il nome del giocatore: ")
    squadraX = verifica_giocatore_in_squadra(squadre, giocatoreX)
    print(f"Il giocatore {giocatoreX} gioca al {squadraX}")

    gX = input("Inserisci il nome del giocatore da trasferire: ")
    sX = input("Inserisci il nome della nuova squadra: ")
    trasferire(squadre, gX, sX)

if __name__=="__main__":
    main()