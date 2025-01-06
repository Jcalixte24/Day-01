#liste dans l'ordre chronologique des albums de damso ( pcq c le goat XD )
liste=["Batterie faible", 'ipséité',"lithopédion","Qalf","Qalf infinity"
       ,"vieux sons","j'ai menti"]

#code 1 de façon libre 
renverse =[]
renverse.append(liste[::-1])#utilisation du slicing
print(renverse)

#code 2 dans une fonction

def renverser(liste):
    return liste[::-1]

#code 3 avec reverse
def renverser2(liste):
    liste.reverse()# on s'attaque directement à la liste dans ce cas 
    return liste
