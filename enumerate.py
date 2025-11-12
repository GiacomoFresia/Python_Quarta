def main():
    lista = ["Alice", "Luca", "Giovanni", "Mario"]
    nome_max = None   # come il NULL in c
    len_max = 0
    for i, nome in enumerate(lista):
        if len(nome) > len_max:
            nome_max = nome
            len_max = len(nome)
    print(nome_max)

def main():
    lista = ["Alice", "Luca", "Giovanni", "Mario"]
    for i, nome in enumerate(lista):
        print(f"{i} - {nome}")

if __name__=="__main__": # __ si chiama dunder(double underscore)
    print(__name__)
    main()