# Date due liste, restituire una nuova lista con gli elementi presenti in entrambe.

def elementi_comuni(lista_a, lista_b):
    lista_elementi_comuni = []
    for el1 in lista_a:
        for el2 in lista_b:
            if el1 == el2 and el1 not in lista_elementi_comuni:
                lista_elementi_comuni.append(el1)
    return lista_elementi_comuni

def main():
    lista_a = [1, 5, 8, 12, 15, 20]
    lista_b = [3, 5, 10, 12, 18, 20, 25]
    lista_elem_comuni = elementi_comuni(lista_a, lista_b)
    print(f"La lista con gli elemnti comuni è: {lista_elem_comuni}")

if __name__=="__main__":
    main()