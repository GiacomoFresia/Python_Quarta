def main():
    lista_nomi = ["Alice", "Luca", "Giovanni", "Mario"]
    lista_voti = [[6, 10, 5],
                  [7, 6],
                  [8, 10, 9, 9],
                  [5, 8]]
    

    # Voglio stampare il voto a fianco di ogni nome
    for nome, voto in zip(lista_nomi, lista_voti):
        print(f"{nome}: {voto}")
    # zip mi permette di ciclare in parallelo su due o più liste


    # - Stampare la media di ognuno
    for nome, voto in zip(lista_nomi, lista_voti):
        somma = 0
        for voti in voto:
            somma = somma + voti
        k = len(voto)
        media = somma / k
        print(f"{nome} Media: {media}") 


    # - Stampare il numero di voti per ognuno
    for nome, voto in zip(lista_nomi, lista_voti):
        k = len(voto)
        print(f"{nome} Numero di voti: {k}")


    # - Stampare il voto massimo e il voto minimo
    for nome, voto in zip(lista_nomi, lista_voti):
        voto_max = voto[0]
        voto_min = voto[0]
        for voti in voto:
            if voti > voto_max:
                voto_max = voti
            if voti < voto_min:
                voto_min = voti
        print(f"{nome} Voto max: {voto_max} Voto min: {voto_min}")


if __name__=="__main__": # __ si chiama dunder(double underscore)
    main()