from math import * # permettre à l'utilisateur d'utiliser tout type de nobre 
def calculatrice(nombre1,op,nombre2):
    """
    Cette fonction prend en entrée deux nombres et une opération, puis renvoie le résultat
    de l'opération effectuée sur les deux nombres.
    nombre1 : un nombre réel quelquonque
    op : opération a éffectuer écrit sous forme de chaine de caractere

    nombre2 :un nombre réel quelquonque

    """
    
    
    if op == "+":
        return nombre1 + nombre2
    elif op == "-":
        return nombre1 - nombre2
    elif op == "*":
        return nombre1 * nombre2
    elif op == "/":
        if nombre2 != 0:
            return nombre1 / nombre2
        else:
            return "Erreur : division par zéro"
    
