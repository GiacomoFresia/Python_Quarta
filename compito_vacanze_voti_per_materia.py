# Un dizionario associa nomi di materie a liste di voti. Scrivere funzioni per: (a) calcolare
# la media di una materia, (b) trovare la materia con media più alta, (c) aggiungere un
# voto a una materia.

def calcola_media_materia(voti_materie, materiaX):
    somma = 0
    voti = voti_materie[materiaX]
    for voto in voti:
        somma = somma + voto
    media = somma / len(voti)
    return media

def materia_media_piu_alta(voti_materie):
    media_max = 0
    materia_max = ""
    somma = 0
    for materia in voti_materie:
        voti = voti_materie[materia]
        for voto in voti:
            somma = somma + voto
        media = somma / len(voti)
        if media > media_max:
            media_max = media
            materia_max = materia
    return materia_max

def aggiungi_voto(voti_materie, materiaX, votoX):
    voti = voti_materie[materiaX]
    voti.append(votoX)
    return voti

def main():
    voti_materie = {
    "Matematica": [6, 7, 5, 8, 7],
    "Italiano": [7, 8, 7, 6],
    "Inglese": [8, 8, 9, 7, 8],
    "Informatica": [9, 8, 9, 10, 8]
    }

    materiaX = input("Inserisci la materia: ")
    media_materiaX = calcola_media_materia(voti_materie, materiaX)
    print(f"La media della materia {materiaX} è {media_materiaX}")

    materia_max = materia_media_piu_alta(voti_materie)
    print(f"La materia con la media più alta è: {materia_max}")

    materiaX1 = input("Inserisci la materia: ")
    votoX = int(input("Inserisci il voto: "))
    nuovi_voti = aggiungi_voto(voti_materie, materiaX1, votoX)
    print(f"I nuovi voti della materia {materiaX1} sono: {nuovi_voti}")

if __name__=="__main__":
    main()