# Dato un dizionario che associa nomi di studenti ai loro voti (un voto per studente),
# trovare quale voto compare più spesso.

studenti_voti = {
"Marco": 7,
"Sara": 8,
"Luca": 6,
"Elena": 8,
"Paolo": 7,
"Giulia": 8,
"Andrea": 6,
"Chiara": 7
}

cont_voti = {}

for studente in studenti_voti:
    voto = studenti_voti[studente] 
    if voto in cont_voti:
        cont_voti[voto] = cont_voti[voto] + 1 
    else: 
        cont_voti[voto] = 1 
print(cont_voti)

frequenza_max = 0
for voto in cont_voti:
    if cont_voti[voto] > frequenza_max:
        frequenza_max = cont_voti[voto]
        voto_max = voto

print(f"Il voto più frequente è il {voto_max} con una frequenza di {frequenza_max}")