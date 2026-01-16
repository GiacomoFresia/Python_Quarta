# Il file simulazione_verifica1.txt contiene informazioni sugli studenti di una scuola. 
# Ogni riga del file ha il seguente formato:
# nome classe voto1 voto2 voto3. Scrivere un programma Python che:
# Legga il file e crei una lista di dizionari, in cui ogni dizionario rappresenta uno studente nel seguente formato:
# {
   # "nome": "Marco",
    #"classe": "1A",
   # "voti": [6, 7, 8]
#}
#Scriva una funzione che, data la lista di dizionari:
#calcoli la media dei voti di ogni studente
#aggiunga al dizionario dello studente la chiave "media"

#Crei un dizionario di liste che associ ad ogni classe la lista delle medie degli studenti di quella classe.
#Scriva una funzione che:
#calcoli la media della classe
#stampi la classe con la media più alta
#Stampi tutti gli studenti con media ≥ 6, il nome dello studente con la media più bassa

def media1():
    file = open("simulazione_verifica1.txt", "r", encoding="utf8")
    righe = file.readlines()
    file.close()

    l = []
    medie = []
    cont = 0
    diz_medie_studenti_classe = {}
    l_classe_1 = []
    l_classe_2 = []

    for i in righe:
        parole = i.split(" ")
        diz = {"nome": parole[0], "classe": parole[1], "voti": parole[2:]}
        l.append(diz)

        somma = 0
        for a in range(2, 2 + len(parole[2:])):
            somma += int(parole[a])
        medie.append(somma / len(parole[2:]))

        diz["media"] = medie[cont]

        if parole[1] == "1A":
            l_classe_1.append(medie[cont])
            diz_medie_studenti_classe["1A"] = l_classe_1
        else:
            l_classe_2.append(medie[cont])
            diz_medie_studenti_classe["1B"] = l_classe_2

        cont += 1

    print("MEDIE: ", medie)
    print(l)
    print(diz_medie_studenti_classe)

def main():
    media1()

if __name__=="__main__":
    main()