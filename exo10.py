notes = input("entrez plusieurs notes séparées par des virgules:")
# on utilise une liste par compréhension

notes = [int(note) for note in notes.split(",")] # on convertit les nombre données sous forme de liste en se basant sur les virgules

somme=0

for i in range (len(notes)) :
    somme += notes[i]
print("la moyenne est :" , somme / len(notes))
    

