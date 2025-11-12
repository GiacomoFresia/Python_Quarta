# Scrivi un programma in Python nel quale assegni alla variabile lista_voti
# una lista con tutti i tuoi voti(almeno 6 voti). Sfrutta l'indicizzazione per:
# -stampare la lista senza il primo e l'ultimo voto;
# sostituire il quarto voto con un 10;
# stampare i primi 3 voti della lista.

lista_voti = [3, 6, 10, 2, 9.5, 7.5]
print(f"La lista senza il primo e l'ultimo voto è {lista_voti[1:-1]}")

print(f"I primi 3 voti della lista sono {lista_voti[0:3]}")

lista_voti[3] = 10
print(f"La lista con il quarto voto sostituito è{lista_voti}")