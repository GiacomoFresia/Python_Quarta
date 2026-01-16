# Scrivere un programma in Python che legga il contenuto di un file di testo chiamato studenti.txt, 
# in cui ogni riga contiene il nome di uno studente e il relativo voto separati da uno spazio. 
# Il programma deve chiedere all’utente di inserire un voto minimo e creare un nuovo file chiamato promossi.txt 
# contenente solo le righe degli studenti che hanno ottenuto un voto maggiore o uguale al voto minimo inserito. 
# Il programma deve utilizzare almeno una funzione, un ciclo for e la gestione dei file.

def nuovo_file(voto_minimo):
    file = open("studenti.txt", "r", encoding='utf-8')
    testo = file.read()
    file.close()

    righe = testo.split("\n")
    nuovo = open("promossi.txt", "w", encoding='utf-8')
    for riga in righe:
        if riga != "":
            parti = riga.split(" ")
            if int(parti[1]) >= voto_minimo:
                nuovo.write(riga + "\n")
    nuovo.close()

def main():
    voto_min = int(input("Inserisci il voto minimo: "))
    nuovo_file(voto_min)

if __name__=="__main__":
    main()