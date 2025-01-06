from random import randint

nombre =randint(1,100)# choix aléatoire du nombre

while True :
    user= int(input('entrez votre nombre :'))
    
    if user > nombre :
        print("votre nombre est trop grand")
    
    elif user < nombre :
        print("votre nombre est trop petit")
    
    else :
        print("Bravo ! Vous avez trouvé le nombre.")
        break# si le nombre est trouvé la fonction s'arrete

