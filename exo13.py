nombre = input("Entrer une liste de nombres séparés par des virgules : ")
liste = [int(x) for x in nombre.split(",")]  # Création de la liste par compréhension

for i in range(len(liste)):
    for j in range(1, len(liste)-i-1): 
        if liste[j] > liste[j+1]:
            liste[j], liste[j+1] = liste[j+1], liste[j]  # Permutation des éléments

print(liste)  # Affichage de la liste triée
