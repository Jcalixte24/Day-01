import random
def gen_mdp(longueur):
    #initialisation de nos caracteres
    caracteres="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@!§?/:%"
    mdp=''
    for i in range (longueur):
        mdp+=random.choice(caracteres)#choix aléatoires parmis les caracxteres donnes
    return mdp

longueur = int (input('Entrez la longueur du mot de passe : '))
print("le mot de passe est : ", gen_mdp(longueur))


