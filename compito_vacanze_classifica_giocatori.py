# Una lista contiene dizionari con chiavi nome, punteggio. Scrivere una funzione che
# stampi la classifica ordinata per punteggio decrescente, numerando le posizioni.

def classifica(giocatori):
    for i in range(len(giocatori)):
        max = i
        for j in range(i, len(giocatori)):
            if giocatori[j]["punteggio"] > giocatori[max]["punteggio"]:
                max = j
        temp = giocatori[i]
        giocatori[i] = giocatori[max]
        giocatori[max] = temp
        print(f"{i}. --> {giocatori[i]}")

def main():
    giocatori = [
    {"nome": "Player1", "punteggio": 4500},
    {"nome": "Player2", "punteggio": 7200},
    {"nome": "Player3", "punteggio": 3100},
    {"nome": "Player4", "punteggio": 8900},
    {"nome": "Player5", "punteggio": 5600}
    ]
    print(classifica(giocatori))

if __name__ == "__main__":
    main()