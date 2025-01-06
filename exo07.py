ph=input("Entrez votre phrase :")
voyelles=['a','e','i','o','u','y','A','E','I','O','U','Y'] # definition des voyelles
cpt = 0
affichage=[]#liste qui va contenir les voyelles
for i in ph :# on parcourt les élements de la phrase 
    if i in voyelles :
        cpt += 1
        if not i in affichage :
            affichage.append(i)
print ("les voyelles présentes sont : ", affichage, "le nombre de voyelle est :",cpt)

