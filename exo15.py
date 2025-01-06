from random import randint 
def nb_mystere():
    mystere= randint(1,1000) #choix du nombre
    cpt = 0
    while cpt < 10 :
        user =int(input("entrez un nombre :"))
        cpt +=1
        if user < mystere :
            print("le nombre est trop petit")
            
        if user > mystere : 
            print("le nombre est trop grand")
        if user == mystere :
            print("vous avez trouve le nombre mystere")
            break
        
nb_mystere()
    

