#Simulare n partire pari e dispari.
#Input utente:
#- n numero di partite.
#- nome primo giocatore.
#- nome secondo giocatore.

#1) Per simulare le partite usiamo un dizionario:
#esempio nel caso n = 3
#d = {"Nome giocatore 1": [3,2,5], "Nome giocatore 2": [1,4,4]"}
#Le singole giocate sono generate con random.randint()

#2) Creare una lista che contiene i nomi dei vincitori per ogni partita e stamparla

#Ipotesi: il primo giocatore è sempre il pari ed il secoondo è sempre dispari


#nomi = ['Luca', 'Mario', 'Alice']
#voti = [5, 7, 10]

#nome = input("Dammi un nome: ")

#diz = {}
#for n, v in zip(nomi, voti):
#    diz[n] = v

#print(f"Il voto di {nome} è {diz[nome]}")


import random

MINIMO = 0
MASSIMO = 5

def simulaPartite(partite):
     lanci = []
     for _ in range(partite):
          lanci.append(random.randint(MINIMO, MASSIMO))
     return lanci
          
def main():

     numeri = []

     partite = int(input("Dammi il numero di partite che vuoi giocare: "))
     nome1 = input("Dammi il nome del primo: ")
     nome2 = input("Dammi il nome del secondo: ")

     d = {nome1 : simulaPartite(partite), nome2 : simulaPartite(partite)}
     print(d)

     vincitori = []

     for mano1, mano2 in zip(d[nome1], d[nome2]):
          if(mano1 + mano2) % 2 == 0:
               vincitori.append(nome1)
          else:
               vincitori.append(nome2)


     print(vincitori)
     

     
if __name__ == "__main__":
     main()